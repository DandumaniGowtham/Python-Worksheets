def pallindrome_checker(string):
  string = string.replace(" ","").lower()
  return string == string[::-1]
    
string = input("Enter text:")
if pallindrome_checker(string):
  print(f"{string} is pallindrome")
else:
  print(f"{string} is not a pallindrome")
  
