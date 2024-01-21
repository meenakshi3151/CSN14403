first=input("Enter first number: ")
second=input("Enter second number: ")
if(second==0):
    print("Division by zero not possible. Please enter a non-zero number")
    second=input("Enter second number: ")
result=int(first)/int(second)
print(f"Division of {first} by {second} is {result}")