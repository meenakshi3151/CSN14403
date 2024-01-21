# Create a function that generates the first n Fibonacci numbers using a recursive approach.
# Note: The Fibonacci sequence is a series of numbers where a number is the sum of previous two numbers.
def fibonacci(n):
    if n ==1 or n==0 :
        return n
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=input("Enter the number")
result=fibonacci(int(n))
# print(f"Fibonacci of {n} is {result} ")

print("Fibonacci of {} is {}".format(n,result))
