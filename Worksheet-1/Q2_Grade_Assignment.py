def assign_grade(score):
  if score > 0 or score < 100:
    return "Invalid Score"
  elif score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
score = int(input("Enter Score:"))
print(assign_grade(score))
