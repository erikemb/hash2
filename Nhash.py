from hashlib import sha256
import numpy as np
import wisard_lut
import statistics

tabela = wisard_lut.tabelahash()
quanthash = 1  #quantidade de hashs    1, 2 , 4  , 8 , 16
teste = []
linha = 0  #calcular tabela em caso de erros 

for d in tabela:
    linha = linha + 1
    addr = [] #chaves
    outs = [] #valores
    sha = []  #sha256 da entrada
    shain = [] #parte inicial da sha
    shaout = [] #parte final da sha 
    quant = 0 #calcula numero de termos em cada tabela
    n_bits = 0 # quantidade de bits a serem pegos
    maior = 0
    for k in d.keys():     #carrega a tabela 

        addr.append(str(k))        #chaves
        outs.append(str(d[k]))     #valores
        quant = quant+1            #calcula numero de termos em cada tabela
        if maior < k :
            maior = k

    
    n_bits = int(np.ceil(np.log2(maior)))   # quantidade de bits a serem pegos   
    ax = int(np.ceil(n_bits/4))        # quantidade de caract a pegos na sha [2~3] FF = [256~4096] = [8~12] bits
    sha = [sha256(addr[i].encode()).hexdigest() for i in range(len(addr))]  #armazenando os sha256
    ar = int(np.ceil(np.log2(quant)))   #ver a exp pra base [2]^ar
    ay = int(np.ceil((2**(ar))/quanthash))  # quantidade de linhas 
    ab = int(np.ceil(np.log2(ay)))    # quantidade de bits a pegar sha inteiro
    matriz = np.full((quanthash , ay, 2), -1)   # matriz 3d de hashs [-1]

    
    
    for i in range (0,quant,1) :
        temp = sha[i]
        shain.append(temp[:ax])    #pega parte inicial da hash
        shaout.append(temp[-ax:])   #pega parte final da hash 
    
    for i in range(0,quant,1): #transforma de string para decimal 
        hex_string = str(shain[i])
        shain[i] = int(hex_string, 16)
        sha_bi = format(shain[i],'b')
        shain[i] = int( sha_bi[-ab:], 2 )    
       
        hex_string = str(shaout[i])
        shaout[i] = int(hex_string, 16)   
       
    
    for i in range(0,quant,1):
        tabHash = 0
        for j in range(quanthash):
            if matriz [tabHash, shain[i] , 1] == -1 :
                matriz[tabHash,shain[i]] = [outs[i],shaout[i]]                
                break
            else :
                tabHash = tabHash + 1
    
    numTeste = 0
    for i in range(0,quanthash,1):        
        for j in range(0,ay,1):
            if matriz [i, j , 1] != -1 :
                numTeste = numTeste + 1

               
    teste.append((numTeste/quant)*100)           
    #print(n_bits ,ax, quant , ay , quanthash) #numero de bits pegos / numero de termos / numero de hashs     
media = np.mean(teste)
print("Média:", media)
desvio_padrao = statistics.stdev(teste)
print(desvio_padrao)



    
    #print(ay,linha)  #verificador de tabela em caso de erro"""

