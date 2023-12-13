def top_str_to_int(balance):
    len_b = len(str(balance))
    balancee = str(balance)
    if len_b == 7:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}M"
        return balance_user
    elif len_b == 8:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}M"
        return balance_user
    elif len_b == 9:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}M"
        return balance_user
    elif len_b == 10:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}B"
        return balance_user
    elif len_b == 11:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}B"
        return balance_user
    elif len_b == 12:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}B"
        return balance_user
    elif len_b == 13:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}T"
        return balance_user
    elif len_b == 14:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}T"
        return balance_user
    elif len_b == 6:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}K"
        return balance_user
    elif len_b == 5:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}K"
        return balance_user
    elif len_b == 4:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}K"
        return balance_user
    elif len_b == 15:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}T"
        return balance_user
    elif len_b == 16:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}q"
        return balance_user
    elif len_b == 17:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}q"
        return balance_user
    elif len_b == 18:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}q"
        return balance_user
    elif len_b == 19:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}Q"
        return balance_user
    elif len_b == 20:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}Q"
        return balance_user
    elif len_b == 21:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}Q"
        return balance_user
    elif len_b == 22:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}s"
        return balance_user
    elif len_b == 23:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}s"
        return balance_user
    elif len_b == 24:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}s"
        return balance_user
    elif len_b == 25:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}S"
        return balance_user
    elif len_b == 26:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}S"
        return balance_user
    elif len_b == 27:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}S"
        return balance_user
    elif len_b == 28:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}O"
        return balance_user
    elif len_b == 29:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}O"
        return balance_user
    elif len_b == 30:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}O"
        return balance_user
    elif len_b == 31:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}N"
        return balance_user
    elif len_b == 32:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}N"
        return balance_user
    elif len_b == 33:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}N"
        return balance_user
    elif len_b == 34:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}d"
        return balance_user
    elif len_b == 35:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}d"
        return balance_user
    elif len_b == 36:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}d"
        return balance_user
    elif len_b == 37:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}U"
        return balance_user
    elif len_b == 38:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}U"
        return balance_user
    elif len_b == 39:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}U"
        return balance_user
    elif len_b == 40:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}D"
        return balance_user
    elif len_b == 41:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}D"
        return balance_user
    elif len_b == 42:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}D"
        return balance_user
    elif len_b == 43:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}Tre"
        return balance_user
    elif len_b == 44:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}Tre"
        return balance_user
    elif len_b == 45:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}Tre"
        return balance_user
    elif len_b == 46:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}Qua"
        return balance_user
    elif len_b == 47:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}Qua"
        return balance_user
    elif len_b == 48:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}Qua"
        return balance_user
    elif len_b == 49:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}Qui"
        return balance_user
    elif len_b == 50:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}Qui"
        return balance_user
    elif len_b == 51:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}Qui"
        return balance_user
    elif len_b == 52:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}SE"
        return balance_user
    elif len_b == 53:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}SE"
        return balance_user
    elif len_b == 54:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}SE"
        return balance_user
    elif len_b == 55:
        balance_str = balancee[0:1]
        balance_user = f"{balance_str}SEP"
        return balance_user
    elif len_b == 56:
        balance_str = balancee[0:2]
        balance_user = f"{balance_str}SEP"
        return balance_user
    elif len_b == 57:
        balance_str = balancee[0:3]
        balance_user = f"{balance_str}SEP"
        return balance_user
    else:
        return balance
