from hashlib import sha256
import numpy as np

ba = 4; # bits entrada
bo = 3; #bits armazenados 
n = 10;  #numeros de entradas 
hash=[]
hash1=[]
hash2=[]
addr = np.random.randint(0,2**ba, (n,1))   #gerando numero de entrada 
outs = np.random.randint(0,2**bo, (n,1))   #gerando numero de saida
print("") #espaçamento

for i in range(len(addr)):
    print(sha256("{0:b}".format(addr[i].tolist()[0]).encode()).hexdigest())    #imprimindo os hash
    hash.append(sha256("{0:b}".format(addr[i].tolist()[0]).encode()).hexdigest())   #armazenando os hash
    
print("")
for i in range(len(addr)):  #imprime entrada 
    print(addr[i])
print("")
for i in range(len(outs)):   #imprime saida
    print(outs[i])

print("")
for i in range(len(addr)):
    temp = hash[i]
    hash1.append(temp[:1])    #pega parte inicial da hash
    print(hash1[i])

print("")
print("hash1")
for i in range(1,n,2): #transforma em decimal
    hex_string = hash1[i]
    an_integer = int(hex_string, 16)
    hex_value = hex(an_integer)   
    print(an_integer)

print("")
print("hash2")

for i in range(len(addr)):
    temp = hash[i]
    hash2.append(temp[-1])    #pega parte final da hash
    # print(hash2[i])     # comentar pra ficar melhor de ver

for i in range(1,n,2): #transforma em decimal
    hex_string = hash2[i]
    an_integer = int(hex_string, 16)
    hex_value = hex(an_integer)   
    print(an_integer)

