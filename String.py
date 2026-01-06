str1 ="I love coding.\n"
str2 = "I am practising."
resultStr = str1+str2
print(resultStr)
print(len(str1))
print(len(str2))
print(len(resultStr))

#Indexing
str = "sangita bilawar"
print(str[9])
print(str[7]) #here blank spce is printed
print(str[13])

#Slicing(postive+negative)
str = "shehzad"
print(str[0:4])   #fourth index is not included
print(str[:3])    #starts from beginning
print(str[3:])     #End at last index
print(str[::])      #Start from beginning up to end

str = "Apple"
print(str[-4:-1])
print(str[-5:-4])
print(str[-5:-1])
