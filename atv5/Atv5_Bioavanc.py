fl = open("rosalind_ini5.txt", "r")
arq = open("resposta.txt", "a")
read = fl.readlines()

for i in range(1, len(read), 2):
	arq.write(read[i])

fl.close()
arq.close() 
