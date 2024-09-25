# Encoded message:
Encoded_Message = "##$$$@!yalpstcejorp EPUVT****9887"

# Extract the core part of the message: 
Core_Message = Encoded_Message[7:25]

# Reverse the first word: "yalpstcejorp":
First_Word = Core_Message[12::-1]
print(First_Word)

# Replace E->A, U->O to get "APOVT".
Second_Word = Core_Message[12:].replace('E','A').replace('U','O')
print(Second_Word) 

#Final decoded message
print(f"Final decoded message : {First_Word}{Second_Word} ")