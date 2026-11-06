"""
File type check
Take a filename as input(like report.pdf). 
Check if it ends .pdf, .docx, or .txt 
and print the file type.
else print invalid.
"""
filename = input("Enter filename(e.g: report.pdf): ")
if filename.endswith(".pdf") or filename.endswith(".docx") or filename.endswith(".txt"):
    print("Valid")
else: 
    print("Invalid")

