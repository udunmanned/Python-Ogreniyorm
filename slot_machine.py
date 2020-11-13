from random import*

slot_items=["Muz","Bomba","Kedi","Elma"]

slot_case=""

response=input("Slot Oynamak İster Misiniz=")

while response=="evet":
  win_rat=""
  print("*"*15)
  slot_case=""
  print("Hoşgeldiniz..")
  print("Döndürülüyor...")

  for _ in range(1,4):
   slot_fill=slot_items[randint(0,3)]
   slot_case="|"+slot_fill+"|"+slot_case
   x=(slot_case[_])
   win_rat=x+win_rat
   print(win_rat[::1])
      
  print(slot_case)

  if win_rat[::1]== "moB" and "mlE" and "deK" and "zuM" :
        print("Kazandınız")
  else : 
      print("Kazanamadınız")

  response=input("Bir Daha Oynamak İster Misiniz=")


if response=="hayır":
  print("Yine bekleriz.")
