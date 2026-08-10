def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters")

    if not any(char.isupper() for char in password):
        errors.append("At least one Uppercase letter required")

    if not any(char.islower() for char in password):
        errors.append("At least one lowercase letter required")

    if not any(char.isdigit() for char in password):
        errors.append("At least One digit required")

    if not any(char in "!@#$%^&*" for char in password):
        errors.append("At least one special character reqired")
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }

password = input("Enter password: ")
print(validate_password(password))



# def validate_password(password):
#     errors = []
#     if len(password) < 8:
#         errors.append("At least 8 characters")
#     uppercase = False
#     lowercase = False
#     digit = False
#     special = False
#     for char in password:
#         if char.isupper():
#             uppercase = True
#         if char.islower():
#             lowercase = True
#         if char.isdigit():
#             digit = True
#         if char in "!@#$%^&*":
#             special = True
          
#     if not uppercase:
#         errors.append("At least one uppercase letter require")
#     if not lowercase:
#         errors.append("At least one lowercase letter require")
#     if not digit:
#         errors.append("At least one digit require")
#     if not special:
#         errors.append("At least one special character require")
      
#     return {
#         "is_valid": len(errors) == 0,
#         "errors": errors
#     }
  
# password = input("Enter password: ")
# print(validate_password(password))
