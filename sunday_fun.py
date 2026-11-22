def sunday(day: str) -> None:
    if day == "sunday":
        print(f"You're lucky! Today is sunday (',')")
        print(f"Have a beautiful reset day!!!")
        print(f"Recharge your energy (*,*)")
    elif day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday":
        print(f"I know most people's mind condition will be like this (@,@)")
        print(f"But,")
        print(f"Keep working! Wait for sunday!")
    else:
        raise ValueError(f"Please, enter correct day name.")

day = input("Enter any day of week: ").strip().lower()
sunday(day)