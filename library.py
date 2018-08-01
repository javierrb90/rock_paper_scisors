ROCK=1
PAPER=2
SCISORS=3

def parse_hand_value(hand):
    if hand==ROCK:
        return "ROCK"
    if hand==PAPER:
        return "PAPER"
    if hand==SCISORS:
        return "SCISORS"
    else:
        return "...what are you doing"    

def ask_hand(foo):
    prev_hand=input(foo)
    if not is_number(prev_hand):
        while not is_number(prev_hand):
            prev_hand=input("Dame un número del 1 al 3\n"+foo)
    return int(prev_hand)

def random_hand(min=1,max=3):
    from random import randint
    return randint(min,max)

def compare_hands(hand_A,hand_B):

    if hand_A==ROCK:
        if hand_B==SCISORS:
            return True

    if hand_A==PAPER:
        if hand_B==ROCK:
            return True

    if hand_A==SCISORS:
        if hand_B==PAPER:
            return True

    # hand_A loses or it's the same as hand_b
    return False

def is_number(foo):
    try:
        return int(foo)
    except ValueError:
        return False