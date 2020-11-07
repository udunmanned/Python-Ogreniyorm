##Calculates number of camelcase words
word=input("Please camelcase a word:")
word_low=word.lower()
n=len(word)
letter=0;
counter=0;

while letter<n:
  if word[letter]==word_low[letter]:
   letter=letter+1
  else :
    counter=counter+1
    letter=letter+1
print(counter+1)
