import numpy as np
def teste4() :
    from hashlib import sha256
    import numpy as np


    ba = 16; # bits entrada
    bo = 10; #bits armazenados 
    n = 4000;  #numeros de entradas

    sha=[]  #sha256 da entrada
    shain=[] #parte inicial da sha
    shaout=[] #parte final da sha 
    arm1=[]  #união shain bo shaout
    hash1 = [] 
    hash11 = [] #testador de repetição do hash1
    hash2 = []
    hash22 = [] #testador de repetição do hash2
    hash3 = [] 
    hash33 = [] #testador de repetição do hash3
    hash4= []
    hash44 = [] #testador de repetição do hash4

    m = n / 4

    addr = np.random.randint(0,2**ba, (n,1))   #gerando numero de entrada 
    outs = np.random.randint(0,2**bo, (n,1))   #gerando numero de saida

    n_bits = np.ceil(np.log2(n))   #calcula numero de bits a serem pegos da hash
    a = int(np.ceil(n_bits/4))

    for i in range(len(addr)):
        sha.append(sha256("{0:b}".format(addr[i].tolist()[0]).encode()).hexdigest())   #armazenando os sha256

    for i in range(len(addr)):
        temp = sha[i]
        shain.append(temp[:a])    #pega parte inicial da hash
        shaout.append(temp[-a:])   #pega parte final da hash   

    for i in range(0,n,1): #transforma em decimal
        hex_string = shain[i]
        shain[i] = int(hex_string, 16)
        hex_string = shaout[i]
        shaout[i] = int(hex_string, 16)   
        

    for i in range(0,n,1):
            temp = [shain[i]],[np.int(outs[i])],[shaout[i]]
            arm1.append(temp)

    for i in range(0,n,1) :
        if (shain[i] not in hash11) and (len(hash1))<m:
            hash11.append(shain[i])  
            hash1.append(arm1[i])
        
    for i in range(0,n,1) :  
        if (arm1[i] not in hash1) and (shain[i] not in hash22) and (len(hash2))<m:
            hash22.append(shain[i])  
            hash2.append(arm1[i])

    for i in range(0,n,1) :  
        if (arm1[i] not in hash1) and (arm1[i] not in hash2) and (shain[i] not in hash33) and (len(hash3))<m:
            hash33.append(shain[i])  
            hash3.append(arm1[i])

    for i in range(0,n,1) :  
        if (arm1[i] not in hash1) and (arm1[i] not in hash2) and (arm1[i] not in hash3) and (shain[i] not in hash44) and (len(hash4))<m:
            hash44.append(shain[i])  
            hash4.append(arm1[i])

    tax = 100 * (len(hash1)+len(hash2)+len(hash3)+len(hash4)) / len(arm1)

    return tax

loop = 500
numeros = []
for i in range(loop):  
    numeros.append(teste4())

media = np.mean(numeros)
desvio = np.std(numeros)
print("A média é:", media)
print("O desvio padrão é:", desvio)

#A média é: 96.62329999999999
#O desvio padrão é: 0.2500242188268967
