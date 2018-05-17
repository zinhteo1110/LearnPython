#su dung cach sys.stdout thi di kem la ham print, nhung print se xuat hien them 1 dong empty. Khong dung yeu cau
import sys
filepath = '/usr/src/freeswitch/repository-original.txt'
#sys.stdout=open("repository3.txt","w")
file=open("repository3.txt","w") #mo file can write
with open(filepath) as infile:
	for line in infile:
		if not line.strip():
			continue
		else:
			#print 'http://files.freeswitch.org/yum-1.6/7/x86_64/'+line
			file.write('http://files.freeswitch.org/yum-1.6/7/x86_64/'+line)
#sys.stdout.close()
file.close()
