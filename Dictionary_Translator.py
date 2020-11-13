dictionary={
  "pen":"kalem",
  "book":"kitap",
  "water":"su",
  "this":"bu",
  "is":"olmak",
  "a":"bir"
}

while True :
  sentence_eng=input("İngilizce Bir Cümle Giriniz:")
  if sentence_eng=="":
    print("Teşekkürler")
    break

  else:
    for signCharacters in ".,:?;!":
     sentence_eng=sentence_eng.replace(signCharacters,"")
  
    words=sentence_eng.split()

    for word in words:
      wordMeanings=dictionary.get(word,"[ANLAM BULUNAMADI]")
      print(f"{word} : {wordMeanings}")

