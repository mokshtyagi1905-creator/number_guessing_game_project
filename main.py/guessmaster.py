import random
while True:

  print("----------------------------------")
  print("              WELCOME             ")
  print("----------------------------------")

  print("         GUESSMASTER V1.0         ")

  print("----------------------------------")
  print("              RULES               ")
  print("----------------------------------")
  print("1.Guess a number between 1 and 50")
  print("2.You have unlimited attempts")
  print("3.Game will give you too high and too low hints")
  print("----------------------------------")

  secret= random.randint(1,50)

  x=int(input("try any number between 1 and 50: "))
  attempt=0

  while True:

   if x>50 or x<1:
     print("wrong input:")
   elif x>secret:
      print("Too high!!")
      attempt+=1
      print("attempt:",attempt)
   elif x<secret:
      print("Too low!!")
      attempt+=1
      print("attempt:",attempt)
   else:
      print("congratulations!!")
      print("You guessed right number")
      attempt+=1
      break
   
   x=int(input("try again:"))

  print("------------")
  print("Final Report")
  print("------------")
  print("Total Attempts:",attempt)
  print("secret number:",secret)
  if 1<=attempt<=3:
   print("Amazing! You are a guessing master!🏆")
  elif 4<=attempt<=6:
   print("Great job! You have strong guessing skills.⭐")
  elif 7<=attempt<=10:
   print("Nice work! You solved it with patience.!👍")
  elif 11<=attempt<=15:
   print("Good effort! Keep practicing.🙂")
  elif 16<=attempt<=25:
   print("You got it, but try to use the hints better next time.😅")
  else:
   print("You finally solved it! Try to improve your strategy.🐢")

  print("Wanna play again(y/n)??")
  choice=input("type:")
  if choice.lower()=="y":
    continue
  elif choice.lower()=="n":
    break
  else:
    print("wrong input. Game ends!!")
    break
print("Thank You!!")