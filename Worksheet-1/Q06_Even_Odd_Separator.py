def separate_even_odd(numbers):
  even = []
  odd = []
  for num in numbers:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  return (even, odd)

n = int(input("Enter size of list: "))
numbers = []
for i in range(n):
  numbers.append(int(input()))
even, odd = separate_even_odd(numbers)
print(even)
print(odd)
            
