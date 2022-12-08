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
hash3=[]
hash4=[]
hashc=[]

addr = np.random.randint(0,2**ba, (n,1))   #gerando numero de entrada 
outs = np.random.randint(0,2**bo, (n,1))   #gerando numero de saida