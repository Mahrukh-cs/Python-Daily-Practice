text = "Programming"
print(text[0:4])
print(text[3:8])
print(text[:5])
print(text[5:])
print(text[3:7])
print(text[::2])
# reversed order
print(text[10::-1])
print(text[::-1])



# Practical Eg
email = "mano@gmail.com"
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
print(f"username = {username}")
print(f"domain = {domain}")