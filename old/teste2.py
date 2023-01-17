def teste22():
    from hashlib import sha256
    import numpy as np

    ba = 16; # bits entrada
    bo = 10; #bits armazenados 
    n = 4000;  #numeros de entradas 
    a = 3; # numero de caracteres pegos da hash
    acc = 0 # precisão 
    T = 2000 # termos na hash
    bits = 0

    hash=[]
    hash1=[]
    hash2=[]
    hashc=[]
    addr = np.random.randint(0,2**ba, (n,1))   #gerando numero de entrada 
    outs = np.random.randint(0,2**bo, (n,1))   #gerando numero de saida
  
    for i in range(len(addr)):
        hash.append(sha256("{0:b}".format(addr[i].tolist()[0]).encode()).hexdigest())   #armazenando os hash
       
    for i in range(len(addr)):
        temp = hash[i]
        hash1.append(temp[:a])    #pega parte inicial da hash
        hash2.append(temp[-a:])      

    for i in range(len(addr)):
        hashc.append(str(hash1[i])+str(hash2[i]))
    dup = set(hashc)
    acc = len(dup)
    acc = (acc / n )*100 
    return acc

loop = 1000
media = 0
for i in range(loop):  
    temp = teste22()
    media = media + temp
media = media / loop
print(f' a acc é de  {media:,.2f}%')






