
f=open("/home/hanck/Desktop/fisier1.py","r")
text=" "
l=[ ]
while text != " ":
    text=f.read(10)
    l.append(text)
    print(text)
for i in l:
    print(i)
print(l)
print(text)
f.close()
