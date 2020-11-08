##muz elma ve üzüm
##
fruit=input("Hangi Meyveden İstersiniz:")

if fruit=="muz" or fruit=="Muz" :
  banana_kg=int(input("Kaç Kilo İstersiniz:"))
  banana_price=banana_kg*5 #calculates the banana price
  print(f"Ücret:{banana_price}") # it shows the price

elif fruit=="elma" or fruit=="Elma" :

  color=""
  apple_specs= ["Kırmızı","Sarı","Yeşil","kırmızı","yeşil","sarı"]
  
  while color not in apple_specs :
    print(f"İşte Elma Çeşitlerim:{apple_specs}")
    color=input("Hangisini istersin? = ")
  apple_price= 2 * apple_kg##devam edilecek
  
  