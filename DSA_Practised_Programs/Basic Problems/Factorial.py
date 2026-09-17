num = 5
pro = 1
for i in range(1, num+1):
    pro = pro * i
print(pro)


n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print("Factorial =", fact)