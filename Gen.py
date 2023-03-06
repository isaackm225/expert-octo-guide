import secrets
import string

def gen(param: tuple)->string:
  """Returns a complicated string based on the param"""
  symb,digits,size=param
  pword=""
  tmp=""
  chars = []
  cond=tuple()

  if symb is True:
    chars.append(string.punctuation)
  
  if digits is True:
    chars.append(string.digits)

  chars.append(string.ascii_uppercase)
  chars.append(string.ascii_lowercase)


  for i in range(size*2):
    for char in chars:
      tmp +=str(secrets.choice(char) )

  while not any(cond):
    pword=""
    for i in range(size):
      pword+=secrets.choice(tmp) 
  
      #verification
    if symb and digits:
      if any(c.isdigit() for c in pword) and any(c in string.punctuation for c in pword) and any(c.isupper() for c in pword) and any(c.islower() for c in pword):
        return pword

    elif symb: 
      if any(c in string.punctuation for c in pword) and any(c.isupper() for c in pword) and any(c.islower() for c in pword):
        return pword
    
    elif digits:
      if any(c.isdigit for c in pword) and any(c.isupper for c in pword) and any(c.islower for c in pword):
        return pword
    else:
      pass
  

if __name__=="__main__":
  from UI import ui
  while True:
    print()
    print("Here is your password: {}".format(Gen(ui())))
    print()