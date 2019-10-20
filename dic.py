dict={}
print("empty dictionary")


dict={1:"a",2:"b",3:"c"}
print(dict)

dict={"Name":"a",1:[1,2,3,4]}
print(dict)


Dict=dict({1:"a",2:"b",3:"c"})
print(Dict)


Dict=({1:"a",2:"b",3:{4:"c",5:"d"}})
print(Dict)


dict[0]="a"
dict[1]="b"
dict[2]=1
print(dict)


dict[0]="a"
dict[1]="b"
dict[2]=1
dict['value-set']=2,3,4
print("Dictionary after adding three elements")
print(dict)


dict={1:"a",2:"b",3:"c"}
print(dict[1])


dict={1:"a",2:"b",3:"c"}
print(dict.get(3))


dict={1:"a",2:"b",3:"c"}
del dict[1]
print(dict)


dict={1:"a",2:"b",3:"c"}
dict.pop(1)
print(dict)


dict={1:"a",2:"b",3:"c"}
new=dict.copy()
print(new)


text={1:"a",2:"b",3:"c"}
text.clear()
print(text)


text1={1:"a",2:"b",3:"c"}
text2={4:"d",5:"e",6:"f"}
print(text1)
print(text2)
text1.update(text2)
print(text1)


dic={"name":"a","age":23}
print(dic)
print(str(dic))
print(dic.items())


text1={1:"a",2:"b",3:"c"}
len(text1)


test1={"a":7,"b":1,"c":2} 
print("The dictionary before deletion:"+str(test1)) 
test2=test1.popitem() 
print("The arbitrary pair returned is:"+str(test2)) 
print ("The dictionary after removal:"+str(test1)) 


