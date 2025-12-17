#For loop

colors = ["red","blue","green"]

for color in colors:
    print(color)
print("---------------------")
#range() function

for x in range(1,13,2):
    print(x)
print("---------------------")
#iteration over str

for i in "Python":
    print(i)
print("---------------------")

#nested for loop

for i in range(1,4):
    for j in range(1,4):
        print(i,j)
print("---------------------")

#While loop

i=0
while i<=5:
    print(i)
    i=i+1
print("---------------------")

#break
i=0
while i<=5:
    print(i)
    if i==3:
        break
    i=i+1
print("---------------------")

#continue
i=0
while i<=5:
    print(i)
    if i==3:
        i=i+1
        continue
    i=i+1
print("---------------------")

#pass

for i in range(5):
    pass

print("---------------------")

#DATA STRUCTURES

# list 

list = [1,2,3,4,5]
print(list)
"""for x in list:
    print(x)"""

list.append(29)
list.insert(3,567)
list.remove(5)
list[1]=96
print(len(list))
print(list)


print("---------------------")

#Tuple

tup=("mahek","sayma","zia")

for x in tup:
    print(x)
print("---------------------")

#set

set1={1,2,3,4,5,5,6}

print(set1)
print("---------------------")

#Dictionary

dic = {"name" : "Mahek","surname": "Junnedi","age" : 19}
print(dic)

dic["age"]=18
dic["course"] = "python"

print(dic)
print("---------------------")
