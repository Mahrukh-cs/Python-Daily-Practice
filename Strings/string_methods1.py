"""
strip(): remove leading/trailing
lstrip(): remove leading
rstrip(): remove trailing
"""
text = "      Hi, Everyone!        "
print(text.strip())
print(text.lstrip())
print(text.rstrip())


# practical eg
url = "https://www.google.com/"
clean_url = url.strip("https://")
print(clean_url)


sent = "###Important###"
print(sent.lstrip("#"))
print(sent.rstrip("#"))
print(sent.strip("#"))