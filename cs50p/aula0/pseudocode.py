# Ask the user for their name, remove the spaces from the string, and capitalize the name.
name = input("qual o seu nome ? ").strip().title()

# Split user's name into firts name and last name.
first, last = name.split(" ")

# Say hello to the user.
print("ola. ", first, sep="Como vai, " )