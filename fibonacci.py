#write a program to find fibonacci number of 'n' using function
#fibonacci series 0 1 2 3 5 8........
#fibonacci series 1 2 3 5 8 13........
def fibonacci(n):
  first=0
  second=1
  while n>0:
    third=first+second
    first=second
    second=third
    n-=1
  print(third)
n=int(input("Enter a number: "))
fibonacci(n)
