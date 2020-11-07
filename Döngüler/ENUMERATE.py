index=0
for number in list(range(5,20)) :
  print(f"number:{number},index:{index}")
  index=index+1

##ENUMERATE

for (index,number) in enumerate(list(range(5,15))) : 
  print(f"index:{index} number{number}")