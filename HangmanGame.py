
from random import choice

enterName=input("Please Enter Your Name=> ")

print(f"\nHello {enterName}\nWelcome To The HANGMAN! ")

harf_hakkı=2
health=2
print(f"{health} kelime hakkınız ve {harf_hakkı} harf hakkınız vardır")
guess_list=["kalem","şişe","mikrofon","kutu"]
count=0
current_word=choice(guess_list)

print(f"Şuanki Kelimenin Uzunluğu:{len(current_word)}")
print("*"*15)

while harf_hakkı>0:
 count=0
 log_letter=input("Harf tahminizi giriniz==")  
 if log_letter in current_word:
   harf_hakkı=harf_hakkı-1
   for _ in current_word:
     if log_letter==_:
       count=count+1
   print("Harften",count,"kadar var")
 else:
    print("Malesef Bu Harf Kelimede Yok")
    harf_hakkı=harf_hakkı-1
 print(harf_hakkı,"Harf Hakkın Kaldı")



if harf_hakkı==0:
  while health>0:
    person_guess=input("Kelime Tahmininiz==")
    if person_guess==current_word :
      print("Tebrikler oyunu kazandınız")
      break
    else:
      health=health-1
      print(f"Malesef yanlış\nŞu kadar hakkınız kaldı{health}")
      