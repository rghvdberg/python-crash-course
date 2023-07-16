# Changing Case in a String with Methods

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())


# Combining or Concatenating Strings

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

# print(full_name)

message = "Hello, " + full_name.title() +"!"
print(message)


# Adding Whitespace to Strings with Tabs or Newlines
# tab = \t 
# newline = \n 
print("Hello,"+"\n\t" + first_name.title() + "\n\t\t" + last_name.title())


# Stripping Whitespace

favorite_language = '    python    '
print("No whitespace stripping")
print("My favorite programming language is "+favorite_language+"!")

print("\nlstrip()")
print("My favorite programming language is "+favorite_language.lstrip()+"!")

print("\nrstrip()")
print("My favorite programming language is "+favorite_language.rstrip()+"!")

print("\nstrip()")
print("My favorite programming language is "+favorite_language.strip()+"!")

