import numpy as np

G = np.array([[1,0,0,0,0,1,1], 
	 		  [0,1,0,0,1,0,1],
	 		  [0,0,1,0,1,1,0], 
	 		  [0,0,0,1,1,1,1]],dtype=np.int32)
k = 0

def Hamming_code(array):

	a = np.array(array,dtype=np.int32)
	aux = np.array(np.zeros((1,7)),dtype=np.int32) 
	for i in range(0,7):
		suma = 0
		for j in range(0,4):
			suma = suma +(a[0,j] * G[j][i]) 
		aux[0,i] = int(suma%2);
	return aux 		


spisok = np.array(np.zeros((1,4)),dtype=np.int32)

file = open("encoding.txt","r")
txt = (file.read().rstrip())
file.close() 
elem = 0
res = np.array(np.zeros((1,7)),dtype= np.int32)

file2 = open("Hamming.txt","w");
for ch in txt:
	if ch != '\n':
		spisok[0,elem] = ch
		elem = elem + 1
		if elem == 4:
			res = Hamming_code(spisok)
			for i in range(0,7):
				file2.write(str(res[0,i]))
			file2.write("\n")
			k = k + 1
			elem = 0
file2.close()

print("Кодируем Хэммингом ")
file3 = open("Hamming.txt","r")
file3.close() 



