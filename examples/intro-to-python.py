x = 1
y = x + 5.0001
z = y

print(type(x))
print(type(y))
print(type(z))

b = True
print(type(b))

if b != "True":
  print("True != 'True'")

if b == 1:
  print("But  True = 1??")

s = 'Single Quote String'
d = "Double Quote String"
ds = "'Single in Double Quote String'"
sd = '"Doulbe in Single Quote String"'
print(f" This is interpolted {sd} ")
print([s,d,ds,sd])
print(type(ds))
print(f"This is a list {type([])}" )
sddssd = s+d+ds+sd
print(sddssd)

standard_input = 'hello world'
name = input("Enter Your Name:") 
print(f"Hello {name}")

# val = int(input("Enter A Number:"))
# print(type(val))
# print(f"{val} is quite a number")
val2 = 5.789
print(f"Number as a string {str(val2)}")

# Continue Lines
# first_number = int(input('Type the first number: ')) ;\
# second_number = int(input('Type the second number: ')) ;\
# print("The sum is: ", first_number + second_number)

first_number = int(input('Type the first number: ')) 
second_number = int(input('Type the second number: ')) 
print("The sum is: ", first_number + second_number)
