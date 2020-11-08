turkish_letters=["ğ", "Ğ", "ç", "Ç", "ş", "Ş", "ü","Ü", "ö", "Ö", "ı", "İ" ]

password=str(input("Lütfen Türkçe Karakter İçermeyen Şifre Giriniz:"))
if password in turkish_letters :
  while password in turkish_letters :

   password=str(input("Lütfen Türkçe Karakter İçermeyen Şifre Giriniz:"))
  print("İşlem tamam")
else :
  print("İşlem tamam")