import sys

print(f"Python cvesrion {sys.version}")


#print("gonna read the first 10 chars ")
#a= sys.stdin.read(10)

#for i in range(len(a)):
#	print(a)


print("getting list elements input and performing asome ransdom opetations")

list_elemnts =sys.stdin.readline()

print(list_elemnts)
print(type(list_elemnts))


buffer = ""
list=list()
for i in range(len(list_elemnts)) :
	buffer = buffer + str(list_elemnts[i])
	if list_elemnts[i] == " " or i == len(list_elemnts)-1:
		try:
			list.append(int(buffer.strip()))
			buffer= ""
		except:
			list.append(buffer)
			buffer= ""

print(list)



