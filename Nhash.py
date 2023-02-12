from hashlib import sha256
import numpy as np
import wisard_lut
import sys

tabela = wisard_lut.tabelahash()
quanthash = 2    #quantidade de hashs
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
    
    for k in d.keys():     #carrega a tabela 

        addr.append(str(k))        #chaves
        outs.append(str(d[k]))     #valores
        quant = quant+1            #calcula numero de termos em cada tabela

    
    n_bits = np.ceil(np.log2(quant))   # quantidade de bits a serem pegos
    ax = int(np.ceil(n_bits/4))        # quantidade de caract a pegos na sha [2] FF = 256  ~ 8 bits
    sha = [sha256(addr[i].encode()).hexdigest() for i in range(len(addr))]  #armazenando os sha256
    ay = 2**(ax*4)  # quantidade de linhas 

    matriz = np.full((quanthash , ay, 2), -1)   # matriz 3d de hashs [-1]

    
    for i in range (0,quant,1) :
        temp = sha[i]
        shain.append(temp[:ax])    #pega parte inicial da hash
        shaout.append(temp[-ax:])   #pega parte final da hash 
    
    for i in range(0,quant,1): #transforma de string para decimal 
        hex_string = str(shain[i])
        shain[i] = int(hex_string, 16)
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
    

    """for i in range(quanthash):  #mtd 1 de imp
        for j in range(ay):
            for k in range(2):
                print(matriz[i, j, k], end=' ')   
            print()
        print()

    np.set_printoptions(threshold=sys.maxsize) #mtd 2 de imp
    print(matriz)"""
    
    numTeste = 0
    for i in range(0,quanthash,1):        
        for j in range(0,quant,1):
            if matriz [i, j , 1] != -1 :
                numTeste = numTeste + 1

               
    teste.append(numTeste)            
            
print(teste)





    #print(ay,linha)  #verificador de tabela em caso de erro

