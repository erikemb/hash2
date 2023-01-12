import numpy as np
def teste2():
    from hashlib import sha256
    import numpy as np


    ba = 16; # bits entrada
    bo = 10; #bits armazenados 
    n = 1000;  #numeros de entradas
    sha=[]  #sha256 da entrada
    shain=[] #parte inicial da sha
    shaout=[] #parte final da sha 
    arm1=[]  #união shain bo shaout
    hash1 = [] 
    hash11 = [] #testador de repetição do hash1
    hash2 = []
    hash22 = [] #testador de repetição do hash2


    m = n / 2

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


    """for i in range(len(hash1)):
        print (hash1[i])

    print("")
    for i in range(len(hash2)):
        print (hash2[i])"""""

    tax = 100 * (len(hash1)+len(hash2)) / len(arm1)

    return tax
    
loop = 100
numeros = []
for i in range(loop):  
    numeros.append(teste2())

media = np.mean(numeros)
desvio = np.std(numeros)
print("A média é:", media)
print("O desvio padrão é:", desvio)