num = int(input("Enter a number to check prime or not:"))
isPrime = True
for i in range(2, num //2 + 1):
    if num % i == 0:
        isPrime = False
if isPrime:
    print(f"{num} is Prime Number")
else:
    print(f"{num} is Not a Prime Number")