string = "aeeeeeeeeiou"
count = 0
vowels = "aeiou"
for i in string:
    if i.lower() in vowels:
        count = count + 1
print(f"vowels count is {count}")