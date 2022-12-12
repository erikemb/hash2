from hashlib import sha256
import numpy as np

ba = 4; # bits entrada
bo = 3; #bits armazenados 
n = 10;  #numeros de entradas 
a = 16; # numero de caracteres pegos da hash
acc = 0 # precisão 
T = 5 # termos na hash
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

"""for i in range(len(addr)):
    print(hash[i])

for i in range(len(addr)):
    print(hash2[i])"""


