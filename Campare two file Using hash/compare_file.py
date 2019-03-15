import hashlib
file1 =raw_input("Enter the first file path....    :")
file2 =raw_input("Enter the secound file path...     :")
try :
	f1 = open(file1)
	f2 = open(file2)
	file1hash = hashlib.sha256(f1.read())
	file2hash = hashlib.sha256(f2.read())
	print file1hash.hexdigest()==file2hash.hexdigest()
except IOError:
	print "please input correct path of file.............."
