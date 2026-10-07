# Keyword arguments
def calculate_marks(eng, phy, math, chem, comp, hist=0):
    print(f"Physics  = {phy}")
    print(f"English  = {eng}")
    print(f"Math  = {math}")
    print(f"Chemistry  = {chem}")
    print(f"Computer  = {comp}")
    print(f"History  = {hist}")
    total_marks = eng+phy+math+chem+comp+hist
    print(f"Total_marks = {total_marks}")

calculate_marks(hist=66, math=75, eng=70, comp=75, phy=60, chem=65)
