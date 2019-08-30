
import numpy

iplist=[]
n=int(input("how many : "))
for i in range(n):
	iplist.append(int(input()))
sis=[]
bro=[]
for i in iplist:
	if i not in sis:
		sis.append(i)
	else:
		bro.append(i)

if(len(sis)>len(bro)):
	while(1):
		bro.append(sis.pop())
		if len(sis)==len(bro):
			break
if(len(bro)>len(sis)):
	while(1):
		sis.append(bro.pop())
		if len(sis)==len(bro):
			break	
print(bro)
print(sis)

x=numpy.array(sis)
print(len(numpy.unique(x)))
