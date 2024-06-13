f1 = open("temp.txt",'r')
content_f1 = f1.read()

f2 = open("temp2.txt",'w')
f2.write(content_f1)
f1.close()
f2.close()