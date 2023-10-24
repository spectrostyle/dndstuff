def get_modifier(stat_value):
    if stat_value == 1:
        mod = -5
        return mod
    elif 2 <= stat_value <= 3:
        mod = -4
        return mod
    elif 4 <= stat_value <= 5:
        mod = -3
        return mod
    elif 6 <= stat_value <= 7:
        mod = -2
        return mod
    elif 8 <= stat_value <= 9:
        mod = -1
        return mod
    elif 10 <= stat_value <= 11:
        mod = 0
        return mod
    elif 12 <= stat_value <= 13:
        mod = 1
        return mod
    elif 14 <= stat_value <= 15:
        mod = 2
        return mod
    elif 16 <= stat_value <= 17:
        mod = 3
        return mod
    elif 18 <= stat_value <= 19:
        mod = 4
        return mod
    elif 20 <= stat_value <= 21:
        mod = 5
        return mod
    elif 22 <= stat_value <= 23:
        mod = 6
        return mod
    elif 24 <= stat_value <= 25:
        mod = 7
        return mod
    elif 26 <= stat_value <= 27:
        mod = 8
        return mod
    elif 28 <= stat_value <= 29:
        mod = 9
        return mod
    elif stat_value == 30:
        mod = 10
        return mod
    else:
        mod = "something went wrong in modifier.py"
        return mod
