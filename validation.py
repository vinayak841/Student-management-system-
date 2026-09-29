def valid_roll(roll_no):
    return bool(roll_no.strip())

def valid_name(name):
    return bool(name.strip()) and all(c.isalpha() or c.isspace() for c in name)

def valid_mark(mark):
    return 0 <= float(mark) <= 100
