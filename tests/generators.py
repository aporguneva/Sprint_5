import random
import string

def generate_email():
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@gmail.com"
    return email
    

def generate_password():
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return password
    
