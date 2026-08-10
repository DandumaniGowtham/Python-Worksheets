def convert_case(text, case_type):
    if case_type == "upper":
        return text.upper()
    elif case_type =="lower":
        return text.lower()
    elif case_type == "title":
        return text.title()
    else:
        return "invalid case_type"

text = input("Enter text: ")
case_type = input("Enter case type: ")
print(convert_case(text, case_type))
