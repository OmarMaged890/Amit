# Encoded message
encoded_message = "###!!@mocleW EPGTQ!!!6789"

# Extract the core part of the message
core_message = encoded_message.split('@')[1].split('!!!')[0]

# get last char 'e'
last_char = core_message.split()[1][0]

# Reverse the first word
first_word = core_message.split()[0][::-1] + last_char

# Handle the second word 
second_word = core_message.split()[1][1:]

# decoded message
decoded_message = f"{first_word.capitalize()} {second_word}"

# Output 
print(decoded_message)