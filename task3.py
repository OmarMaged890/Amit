# Encoded Message:
Encoded_Message = "&&&**$gnirtS PLIO!!@1234"

# Extract the core part of the message: 
Core_Message = Encoded_Message.split('$')[1].split('!')[0]
print(f"Core_Message : {Core_Message}")

# get first word and reverse it :
First_Word = Core_Message.split()[0][::-1]
print(f"First_Word : {First_Word}")

# Replace shifted vowels in the second word: Replace I->E and O->U to get "PLEU".
Second_Word = Core_Message.split()[1].replace('I','E').replace('O','U')
print(f"Second_Word : {Second_Word}")

#Final decoded message
print(f"Final decoded message : {First_Word} {Second_Word} ")