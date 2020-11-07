my_tuple=("Berke","Udunman")

for names in my_tuple:
  print(names)

my_dictionary={"Solmaz":"Aşk","Erva":"Huzur"}
## ! my_dictionary.items() yaparsak tupple a benzetiriz
for (key,value) in my_dictionary.items():
  print(value)
  
my_dic_items=my_dictionary.values()
print(my_dic_items)
##rechange
my_dictionary["Berke"]=my_dictionary.pop("Solmaz")
print(my_dictionary)
