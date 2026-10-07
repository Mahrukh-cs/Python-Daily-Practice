# here 'hist' is a default argument
def calculate_marks(eng, phy, math, chem, comp, hist=0):
    print(f"Physics  = {phy}")
    print(f"English  = {eng}")
    print(f"Math  = {math}")
    print(f"Chemistry  = {chem}")
    print(f"Computer  = {comp}")
    print(f"History  = {hist}")
    total_marks = eng+phy+math+chem+comp+hist
    print(f"Total_marks = {total_marks}")

calculate_marks(66, 67, 75, 70, 75, 60)
