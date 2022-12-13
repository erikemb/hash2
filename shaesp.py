from hashlib import sha256
import numpy as np


ba = 4; # bits entrada
bo = 3; #bits armazenados 
n = 8;  #numeros de entradas 

sha=[]
hash1=[]
dec1=[]
hash2=[]

addr = np.random.randint(0,2**ba, (n,1))   #gerando numero de entrada 
outs = np.random.randint(0,2**bo, (n,1))   #gerando numero de saida

n_bits = np.ceil(np.log2(n))   #calcula numero de bits a serem pegos da hash
a = int(np.ceil(n_bits/4))

for i in range(len(addr)):
    sha.append(sha256("{0:b}".format(addr[i].tolist()[0]).encode()).hexdigest())   #armazenando os sha256

for i in range(len(addr)):
    temp = sha[i]
    hash1.append(temp[:a])    #pega parte inicial da hash
    hash2.append(temp[-a:])   #pega parte final da hash   

for i in range(len(addr)):
    print([hash1[i]],outs[i],[hash2[i]])


