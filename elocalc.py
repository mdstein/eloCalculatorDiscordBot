def parse_rank(elo):
    # all at zero rr
    if elo == 'g1':
        return 1000
    elif elo == 'g2':
        return 1100
    elif elo == 'g3':
        return 1200
    elif elo == 'p1':
        return 1300
    elif elo == 'p2':
        return 1400
    elif elo == 'p3':
        return 1500
    elif elo == 'd1':
        return 1600
    elif elo == 'd2':
        return 1700
    elif elo == 'd3':
        return 1800
    elif elo == 'a1':
        return 1900
    elif elo == 'a2':
        return 2000
    elif elo == 'a3':
        return 2100
    elif elo == 'im1':
        return 2200
    elif elo == 'im2':
        return 2290
    elif elo == 'im3':
        return 2400
    elif elo == 'rad':
        return 2650
    else: return 'unknown response'




def projection(games, coef, elo_gain):
    gl = elo_gain
    store = 0
    for i in range(1, games):
        store = elo_gain * ((coef) ** i)
        gl += store

    # error catches
    if (elo_gain <= 0):
        return 0
    if (coef <= 0):
        return 0
    if (games < 0):
        return 0


    return gl


def do_math(rank_parsed_elo: int, current_elo_prog, gains, losses, wr: float):
    current_elo = current_elo_prog + ((gains * wr) - (losses * (1 - wr))) + rank_parsed_elo
    return current_elo


def elo_to_rank(num):
    if 1000 <= num < 1100:
        lb = 1000
        rr = num - lb
        return 'gold 1 ' + str(rr) + ' rr'
    if 1100 <= num < 1200:
        lb = 1100
        rr = num - lb
        return 'gold 2 ' + str(rr) + ' rr'
    if 1200 <= num < 1300:
        lb = 1200
        rr = num - lb
        return 'gold 3 ' + str(rr) + ' rr'
    if 1300 <= num < 1400:
        lb = 1300
        rr = num - lb
        return 'plat 1 ' + str(rr) + ' rr'
    if 1400 <= num < 1500:
        lb = 1400
        rr = num - lb
        return 'plat 2 ' + str(rr) + ' rr'
    if 1500 <= num < 1600:
        lb = 1500
        rr = num - lb
        return 'plat 3 ' + str(rr) + ' rr'
    if 1600 <= num < 1700:
        lb = 1600
        rr = num - lb
        return 'diamond 1 ' + str(rr) + ' rr'
    if 1700 <= num < 1800:
        lb = 1700
        rr = num - lb
        return 'diamond 2 ' + str(rr) + ' rr'
    if 1800 <= num < 1900:
        lb = 1800
        rr = num - lb
        return 'diamond 3 ' + str(rr) + ' rr'
    if 1900 <= num < 2000:
        lb = 1900
        rr = num - lb
        return 'ascendant 1 ' + str(rr) + ' rr'
    if 2000 <= num < 2100:
        lb = 2000
        rr = num - lb
        return 'ascendant 2 ' + str(rr) + ' rr'
    if 2100 <= num < 2200:
        lb = 2100
        rr = num - lb
        return 'ascendant 3 ' + str(rr) + ' rr'
    if 2200 <= num < 2290:
        lb = 2200
        rr = num - lb
        return 'immortal 1 ' + str(rr) + ' rr'
    if 2290 <= num < 2400:
        lb = 2200
        rr = num - lb
        return 'immortal 2 ' + str(rr) + ' rr'
    if 2400 <= num < 2650:
        lb = 2200
        rr = num - lb
        return 'immortal 3 ' + str(rr) + ' rr'
    if 2650 <= num < 3500:
        lb = 2200
        rr = num - lb
        return 'radiant ' + str(rr) + ' rr'
    else:
        return 'unknown response'
