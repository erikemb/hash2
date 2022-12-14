from hashlib import sha256
import numpy as np


ba = 4; # bits entrada
bo = 3; #bits armazenados 
n = 8;  #numeros de entradas 
m = 4; #quantidade armazenada 
hex_string1 = "casa"
sha=[]
hash1=[]
hash2=[]
arm1=[]


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

for i in range(1,n,2): #transforma em decimal
    hex_string = hash1[i]
    an_integer = int(hex_string, 16)
    hash1[i] = an_integer   
    


for i in range(len(addr)):
        temp = [hash1[i]],[np.int(outs[i])],[hash2[i]]
        arm1.append(temp)

for i in range(len(addr)):
    print(arm1[i])

