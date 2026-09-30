def check_age(age):
    
    year =2026
    month = 9
    day = 30

    flag = False
    user_age = 0

    try:
        user_year, user_month, user_day = (int(part) for part in age.split("-"))
    except (AttributeError, ValueError):
        raise Exception("Incorrect data")

    if year - user_year > 16:
        flag = True
    elif year - user_year == 16:
        if month - user_month > 0:
            flag = True
        elif month - user_month == 0:
            if day - user_day > 0:
                flag = True
            else:
                user_age = 15
        else:
            user_age = 15 
    else:
        user_age = year - user_year
    
    if flag:
        return "Access granted"
    else:
        return f"Denied access, need to be 16, but are {user_age}"