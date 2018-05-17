# Open the file with read only permit
f = open('/usr/src/freeswitch/repository.txt', "r");
# use readline() to read the first line
#if lines = f.readlines() --> the variable lines is a list containing all lines in the file.
line = f.readline()
# use the read lien to read further
# If the file is not empty keep reading on line at a time, till the file is empty
while line:
	# in python 2+
	# print line
	# in python 3 print is a builtin function, so 
	print(line)
	# use readline() to read next line
	line = f.readline()
f.close()


