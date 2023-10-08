import random

def generate():
  password_length = get_password_length()
  charackters = {"smallletters": [97,122],
           "capitalletters": [65,90],
           "numbers": [48,57],
           "specialchars1":[33,47],
           "specialchars2": [58,63]}
  letters = []
  amount = find_amount_of_chars(password_length)
  i = 0
  for value in charackters.values():
    letters += createchar(amount[i],value[0],value[1])
    i += 1
  random.shuffle(letters)
  password = "".join(letters)
  print(password)
def createchar(amount, begin, end):
  dezimal = []
  for i in range(amount):
    dezimal.append(random.randint(begin,end))
  letter = []
  for z in dezimal:
    letter.append(chr(z))
  return letter

def find_amount_of_chars(password_length):
  while True:
    max = password_length - (3+3+3+2+2)
    numsl = random.randint(3,max)
    numkl = random.randint(3,max)
    num = random.randint(3,max)
    sc1 = random.randint(2,max)
    sc2 = random.randint(2,max)
    if numsl + numkl + num + sc1 + sc2 == password_length:
      return numsl, numkl, num , sc1, sc2
    
def get_password_length():
  while True:
    password_length = int(input("Bitte geben Sie die länge ihres Passworts ein: "))
    if password_length > 13:
      return password_length
    else:
      print("Das passwort muss mindestens 13 Zeichen lang sein. Sie haben " + str(password_length) + " ausgewählt." )


generate()