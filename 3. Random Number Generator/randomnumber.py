from random import seed
from random import randint

start   =   int(input("From:    "))
end     =   int(input("Till:    "))

Random = randint(start, end)
print()
print("The random number is", Random)