def teste44():
    from hashlib import sha256
    import numpy as np

    ba = 16; # bits entrada
    bo = 10; #bits armazenados 
    n = 1000;  #numeros de entradas 
    a = 3; # numero de caracteres pegos da hash
    acc = 0 # precisão 
    T = 500 # termos na hash
    bits = 0

    hash=[]
    hash1=[]
    hash2=[]
    hash3=[]
    hash4=[]
    hashc=[]

    addr = np.random.randint(0,2**ba, (n,1))   #gerando numero de entrada 
    outs = np.random.randint(0,2**bo, (n,1))   #gerando numero de saida

    for i in range(len(addr)):   
        hash.append(sha256("{0:b}".format(addr[i].tolist()[0]).encode()).hexdigest())   #armazenando os hash

    for i in range(len(addr)):
        temp = hash[i]
        hash1.append(temp[:a])
        hash2.append(temp[16:16+a:1])
        hash3.append(temp[32:32+a:1])
        hash4.append(temp[-a:])

    for i in range(len(addr)):
        hashc.append(str(hash1[i])+str(hash2[i])+str(hash3[i])+str(hash4[i]))
    dup = set(hashc)
    acc = len(dup)
    acc = (acc / n )*100     
    return acc
loop = 1000
media = 0
for i in range(loop):  
    temp = teste44()
    media = media + temp
media = media / loop
print(f' a acc é de  {media:,.2f}%')
