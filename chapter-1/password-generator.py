import random
import string

def generate_password(n):
  # Ensure n is at least 4 so we can include at least one of each character type
  assert(n >= 4), "Password length must be ar least 4"

  password = []
  password.append(random.choice(string.ascii_uppercase))
  password.append(random.choice(string.ascii_lowercase))
  password.append(random.choice(string.digits))
  password.append(random.choice(string.punctuation))

  for i in range(n - 4):
    random_choice = random.choice([0,1,2,3])
    match random_choice:
      case 0:
        password.append(random.choice(string.ascii_uppercase))
        continue
      case 1:
        password.append(random.choice(string.ascii_lowercase))
        continue
      case 2:
        password.append(random.choice(string.digits))
        continue
      case 3:
        password.append(random.choice(string.punctuation))
        continue
      
  random.shuffle(password)
  
  return ''.join(password)

# print(generate_password(3))
print(generate_password(5))
print(generate_password(10))
print(generate_password(14))
print(generate_password(7))
print(generate_password(8))
print(generate_password(9))