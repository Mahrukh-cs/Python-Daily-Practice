def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

ans = can_vote(20)
print(ans)
print(can_vote(15))
