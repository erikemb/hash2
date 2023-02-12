from hashlib import sha256
import numpy as np
import wisard_lut

tabela = wisard_lut.tabelahash()
quanthash = 4    #quantidade de hashs


for d in tabela:
    addr = [] #chaves
    outs = [] #valores
    sha = []  #sha256 da entrada
    shain = [] #parte inicial da sha
    shaout = [] #parte final da sha 
    quant = 0 #calcula numero de termos em cada tabela
    n_bits = 0 # quantidade de bits a serem pegos
    
    for k in d.keys():     #carrega a tabela 

        addr.append(str(k))        #chaves
        outs.append(str(d[k]))     #valores
        quant = quant+1            #calcula numero de termos em cada tabela

    
    n_bits = np.ceil(np.log2(quant))   # quantidade de bits a serem pegos
    ax = int(np.ceil(n_bits/4))        # quantidade de caract a pegos na sha [2] FF = 256  ~ 8 bits
    sha = [sha256(addr[i].encode()).hexdigest() for i in range(len(addr))]  #armazenando os sha256
    ay = ax * 128  # quantidade de linhas 

    matriz = np.full((quanthash , ay, 2), -1)   # matriz 3d de hashs [-1]

    
    for i in range (quant) :
        temp = sha[i]
        shain.append(temp[:ax])    #pega parte inicial da hash
        shaout.append(temp[-ax:])   #pega parte final da hash 

    for i in range(quant): #transforma de string para decimal 
        hex_string = str(shain[i])
        shain[i] = int(hex_string, 16)
        hex_string = str(shaout[i])
        shaout[i] = int(hex_string, 16)   
    
    
    for i in range(quant):
        tabHash = 0
        for i in range(quanthash):
            if matriz [tabHash, shain[i] , 1] == -1 :
                matriz[tabHash,shain[i]] = [outs[i],shaout[i]]
                break
            else :
                tabHash = tabHash + 1



