import random
print("I have chosen a number, choose the desired difficulty and gues the number. I will hint you inbetween. Make sure to do in within the least possible attempts. ")
print("")
print("Choose the Difficulty:")
print("1.EASY (numbers 1-50)")
print("2.MEDIUM (numbers 1-100)")
print("3.HARD (numbers 1-1000)")
print("")
diff=input('Choose the desired Difficulty: ').lower()
if diff in ['easy','1','1.']:
  num=random.randint(1,50)
  print("")
  print("I have choosen the number. Guess it!")
  attempts=0
  while True:
    attempts=attempts+1
    print("Attempt No.",attempts)
    guess=int(input("Enter Guess number: "))
    diffr=num-guess
    if diffr>0:
      print("Your guess is lower.")
    elif diffr<0:
      print("Your guess is higher.")
    else:
      print("Congratulations! You have found the number")
      print("You did guess the number correctly in",attempts, "Attempts")
      break
elif diff in ['medium','2','2.']:
  num=random.randint(1,100)
  print("")
  print("I have choosen the number. Guess it!")
  attempts=0
  while True:
    attempts=attempts+1
    print("Attempt No.",attempts)
    guess=int(input("Enter Guess number: "))
    diffr=num-guess
    if diffr>0:
      print("Your guess is lower.")
    elif diffr<0:
      print("Your guess is higher.")
    else:
      print("Congratulations! You have found the number")
      print("You did guess the number correctly in",attempts, "Attempts")
      break
elif diff in ['hard','3','3.']:
  num=random.randint(1,1000)
  print("")
  print("I have choosen the number. Guess it!")
  attempts=0
  while True:
    attempts=attempts+1
    print("Attempt No.",attempts)
    guess=int(input("Enter Guess number: "))
    diffr=num-guess
    if diffr>0:
      print("Your guess is lower.")
    elif diffr<0:
      print("Your guess is higher.")
    else:
      print("Congratulations! You have found the number")
      print("You did guess the number correctly in",attempts, "Attempts")
      break
else:
  print("Invalid Choice.")