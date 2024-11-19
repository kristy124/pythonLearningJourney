sentence = input("Enter a sentence: ")
print(f"{sentence.upper()}")

paragraph = input("Enter paragraph here: ")
print(f"There are {len(paragraph.split())} words in the paragraph")

is_number = input("Enter a string here: ").isnumeric()
print(is_number)

full_name = input('Enter your full name: ')
name_parts = full_name.split()
initials = ''.join([name_part[0].upper() for name_part in name_parts])
print(f"Your initials are {initials}")