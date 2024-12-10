# Trent Duncan/matt
# 12/10/24
# Validating String Input (Tiered Assignment)

# Are you and your partner working on Level 1, Level 2 or Level 3 today?
# Working on Level...1

prompt = input("Please type something in and I'll tell you if it has only letters (true=only letters and false= theres something thats not a letter in the text):")

message= prompt.isalpha()

if message == True:
    print("Vaild input:", prompt)
else:
    print("Invalid input. Please enter only alphabetic characters.")
