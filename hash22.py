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
print("") #espaçamento

for i in range(len(addr)):
   # print(sha256("{0:b}".format(addr[i].tolist()[0]).encode()).hexdigest())    #imprimindo os hash
    hash.append(sha256("{0:b}".format(addr[i].tolist()[0]).encode()).hexdigest())   #armazenando os hash
    
"""print("")
for i in range(len(addr)):  #imprime entrada 
    print(addr[i])
print("")
for i in range(len(outs)):   #imprime saida
    print(outs[i])"""

print("")
for i in range(len(addr)):
    temp = hash[i]
    hash1.append(temp[:a])    #pega parte inicial da hash
    #print(hash1[i])

print("")
#print("hash1")
for i in range(1,T,1): #imprime em decimal
    hex_string = hash1[i]
    an_integer = int(hex_string, 16)
    hex_value = hex(an_integer)   
    #print(an_integer)

print("")


for i in range(len(addr)):
    temp = hash[i]
    hash2.append(temp[-a:])    #pega parte final da hash
    #print(hash2[i])     # comentar pra ficar melhor de ver

for i in range(1,T,1): #imprime em decimal
    hex_string = hash2[i]
    an_integer = int(hex_string, 16)
    hex_value = hex(an_integer)   
    #print(an_integer)


    

for i in range(len(addr)):
    hashc.append(str(hash1[i])+str(hash2[i]))
dup = set(hashc)
acc = len(dup)
acc = (acc / n )*100 
bits = (ba+bo+4*a+4*a)*n
bits = bits/8
#bits = bits/1024
#bits = bits/1024
print("")
#acc = 100-((100*acc)/T)
print(acc,"%")
print("consumo é :", bits, "bytes")
print("")
"""print(hash1)
print("")
print(hash2)
print("")
print(hashc)"""







# 16 10 1000
# bytes gastos
# acc 
# hash 4