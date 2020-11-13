from random import*

alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
pass_guess=""
password_in=input("Şifrenizi Girin:")

while pass_guess!=password_in :
  pass_guess=""
  for _ in range(len(password_in)):
    guess_letter=alphabet[randint(0,25)]
    pass_guess=str(pass_guess) + str(guess_letter)
  print(pass_guess)
  


