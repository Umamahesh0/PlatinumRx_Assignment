# =========================
# PYTHON SOLUTIONS
# =========================

# Q1: Convert minutes to human readable format

def convert_minutes(minutes):
    hours = minutes // 60
    remaining = minutes % 60
    
    if hours == 0:
        return f"{remaining} minutes"
    elif hours == 1:
        return f"{hours} hr {remaining} minutes"
    else:
        return f"{hours} hrs {remaining} minutes"


# Test
print(convert_minutes(130))
print(convert_minutes(110))


# Q2: Remove duplicates using loop

def remove_duplicates(s):
    result = ""
    
    for char in s:
        if char not in result:
            result += char
    
    return result


# Test
print(remove_duplicates("programming"))
