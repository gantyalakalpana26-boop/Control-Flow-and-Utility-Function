# 1.Control Flow --If-Else Statement
print("If-else statement")
age=int(input("Please enter your age : "))
if age >=18:
    print("You'aree eligible for voting...")
else:
    print("You're not eligible for voting")

# For Loop
print("For Loop")
for i in range(1,5):
    print(i)

#While Loop
print("# While Loop")
i=1
while i<=5:
    print(i)
    i+=1

#Break Statement
print("#Break Statement")
for i in range(10):
    if i==5:
        break
    print(i)

#Continue Statement
print("Continue Statement")
for i in range(1,6):
    if i==3:
        continue
    print(i)


#---Utility Functions---
print("Utility function")

#len()
name="Python"
print(f"Length : {name}")

#max()
numbers=[10,20,30,40,50]
print(f"Max : {max(numbers)}")
#min
print(f"Min : {min(numbers)}")
#sum
print(f"Sum of : {sum(numbers)}")

#abs
print(f"Absolute : {abs(-25)}")

#round
print(f"Round value : {round(10.2567, 2)}")

# type()
print(f"Type of : {type(100)}")





