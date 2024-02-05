import random
from random import choice, randint
from elocalc import do_math, projection, parse_rank, elo_to_rank


def get_response(user_input: str) -> str:
    pr: str = user_input.lower().split(" ")
    cmd = pr[0]
    req = pr[1:]
    if cmd == 'elo':
        print(req)
        if len(req) < 5:
            return 'invalid format. \n format: rank (2 letters, apart from im or rad) current_elo_prog games_to_play_PROJECTED last_elo_gain last_elo_loss winrate'
        print(req[0] + ' rank')
        print(req[1]+ ' elo')
        print(req[2]+ ' games played')
        print(req[3]+ ' gains')
        print(req[4]+ ' losses')
        print(req[5]+ ' wr')
        # parsed elo, current elo prog, projected gains (meth),projected losses (meth), wr)
        if (float(req[5]) < .5):
            cool_elo = int(do_math(parse_rank(req[0]), int(req[1]), projection(int(req[2]), .997, int(req[3])), projection(int(req[2]), 1.003, int(req[4])), float(req[5])))
        else:
            cool_elo = int(do_math(parse_rank(req[0]), int(req[1]), projection(int(req[2]), .997, int(req[3])),
                                   projection(int(req[2]), 1.00, 0), float(req[5])))
        print(cool_elo)

        return elo_to_rank(cool_elo)
    if cmd == 'random':
        return str(random.randint(1,100))
    if cmd == 'roll':
        return str(random.randint(1,6))
    if cmd == 'coinflip':
        result = str(random.randint(1,2))
        if result == '1':
            return 'heads'
        else:
            return 'tails'

