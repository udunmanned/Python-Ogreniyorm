name=input("Bir Cümle Giriniz ")
newlist=[]
sesli_count=0;
sessiz_count=0;
sesli_harfler=["a","e","ı","i","u","ü","o","ö"]

for letter in name.lower():
  if letter in sesli_harfler:
    sesli_count+=1
  else:
    sessiz_count+=1

print(f"Sesli Harf Sayısı:{sesli_count}\nSessiz Harf Sayısı:{sessiz_count}")
  
