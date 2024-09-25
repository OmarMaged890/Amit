email = "Amit_ml@gmail.edu"

# Check input Validation:
def Validation(email):
    if email.count("@") == 1 and '.' in email.split('@')[1] :
        return True
    else:
        return False 

# Extract Username:
def Username(email):
    return email.split('@')[0]

# Extract and return the domain: 
def extract_domain(email):
    domain_part = email.split('@')[1]
    return domain_part.split('.')[0]

# Check for Domain Ending:
def Domain_Ending(email):
    if email.endswith(".com"):
        return "Commercial Domain"
    elif email.endswith(".edu"):
        return "Educational Domain"
    else:
        return "Other Domain"

#Display The Output:
if Validation(email):
    username = Username(email)
    domain = extract_domain(email)
    domain_type = Domain_Ending(email)
else:
    username = "Invalid email",
    domain = None
    domain_type =  None
    
print(f"Username: {username}")
print(f"Domain: {domain}")
print(f"Domain Type: {domain_type}")