##5 KEREDEN SONRA KİTLENEN PROGRAM

count=0

while count<5 :
  count=count+1
  password=input("Şifrenizi Girin")
  if password=="berke4141":
    print("Tebrikler Doğru Şifre")
    break
  else :
    continue

if count==5 :
  print("Hesabınız 30 sn bloke")