first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

full_name = first_name.strip().title() + " " + last_name.strip().title()

print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section.strip().upper())
print("Favorite Subject:", favorite_subject.strip().title())
print("Character Count:", len(full_name))
