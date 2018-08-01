from library import *

player_hand=ask_hand("1-Rock\n2-Paper\n3-Scisors\n")
cpu_hand=random_hand()

print(
    parse_hand_value(player_hand)+
    " VS "+
    parse_hand_value(cpu_hand)
)

if compare_hands(player_hand,cpu_hand):
    print("Player wins!")
else:
    if player_hand==cpu_hand:
        print("Draw...")
    else:
        print("Player loses...")