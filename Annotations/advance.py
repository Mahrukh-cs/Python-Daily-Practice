# for older versions
# from typing import List, Set, Dict
# def max_marks(marks: List[int]) -> int:
#    return max(marks)
def max_marks(marks: list[int]) -> int:
    return max(marks)

def print_list(lst: list[int | str]):
    print(lst)

ans = max_marks([10, 60, 99, 50, 88])
print(ans)
print_list([20, 66, "mano", 33])