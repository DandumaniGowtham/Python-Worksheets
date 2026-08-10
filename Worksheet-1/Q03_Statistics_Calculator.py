def calculate_statistics(list):
  if len(list) == 0:
    return {"mean": 0, "max": None, "min": None, "count": 0}
  return {"mean":sum(list) / len(list), "max": max(list),"min":min(list),"count":len(list)}
  
n = int(input("Enter size of list:"))
numbers = []
for i in range(n):
  numbers.append(int(input()))
print(calculate_statistics(numbers))
