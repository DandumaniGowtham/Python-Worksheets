string = "dad"
if string == string[::-1]:
    print("Pallindrome")
else :
    print("Not")






num = 121

if str(num) == str(num)[::-1]:
    print("Yes")
else:
    print("not")

temp = num
reverse_num = 0
n = 0
while temp > 0:
    n =temp % 10
    reverse_num = reverse_num * 10 + n
    temp = temp // 10
if num == reverse_num:
    print("Number is Pallindrome")
else:
    print("Not")

