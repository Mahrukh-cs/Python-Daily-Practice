"""
accept a string as input.
print its reverse using string slice.
"""
def reverse_string(text):
    return text[::-1]


text = input("Enter string: ")
ans = reverse_string(text)
print(ans)