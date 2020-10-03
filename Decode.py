import numpy as np

H = np.array([[0,1,1],
			  [1,0,1],
			  [1,1,0],
			  [1,1,1],
			  [1,0,0],
			  [0,1,0],
			  [0,0,1]],dtype=np.int32)

spisok = np.array(np.zeros((1,7)),dtype=np.int32)

def sindrome(array):
	a = np.array(array,dtype=np.int32)
	S = [0,0,0]
	for i in range(0,3):
		suma = 0
		for j in range(0,7):
			suma = suma + (a[0,j] * H[j][i])
		S[i] = int(suma%2)
	return S

def decode(array):
	decoded_word=[0,0,0,0]
	for i in range(0,4):
		decoded_word[i] = array[0,i]
	return decoded_word

def errors_in_word(Sindrome,spisok):
	x1 = np.array(np.zeros((1,4)),dtype= np.int32)
	flag = 0
	index = 0

	for i in range(0,7):
		if((Sindrome[0] == H[i][0]) and (Sindrome[1] == H[i][1]) and (Sindrome[2] == H[i][2] )):
			index = i 
			flag = 1

	if(flag == 1):
		print ("Ошибка была допущена в слове "+ str(spisok[0]) +" в бите "+str(index)+"  и была исправлена.")
		if(spisok[0,index]== 1):
			spisok[0,index] = 0
			print (" исправленное слово: " + str(spisok))
		else:
			spisok[0,index] = 1
			print (" исправленное слово: " + str(spisok))
	x1 = decode(spisok)
	return x1


file = open("Hamming.txt","r")
txt = (file.read().rstrip())
file.close()
con = 0
x = np.array(np.zeros((1,4)),dtype= np.int32)
file2 = open("decoding.txt","w")

for ch in txt:
	if ch != '\n':
		spisok[0,con] = ch
		con = con + 1
		if con == 7:
			Sindrome = sindrome(spisok)
			con = 0
			x = errors_in_word(Sindrome,spisok)
			for i in range(0,4):
				file2.write(str(x[i]))
				file2.write("\n");

		file2.write("\n")

file2.close()












