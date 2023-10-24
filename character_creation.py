from dice_rolls import *
from formatting import *
import modifier

char_stats = {
    "name": "",
    "class": "",
    "armor": "nothing",
    "weapon": "nothing",
    "exp": "0",
    "hp": "",
    "strength": 0,
    "dexterity": 0,
    "constitution": 0,
    "intelligence": 0,
    "wisdom": 0,
    "charisma": 0
}


def character_creator():
    terminal_spaces()

    get_name_role()
    name = char_stats["name"]
    stats_to_assign = rolling_start_stats()
    i_stats_to_assign = 0

    while i_stats_to_assign <= 5:
        print(f"Now {name}, to assign your points:")
        for stat_value in stats_to_assign[i_stats_to_assign:-1]:
            print(stat_value, end=", ")
        print(stats_to_assign[-1], ".", sep="")
        print(f"What stat would {name} like to spend {stats_to_assign[i_stats_to_assign]} points on?")

        for stat_type in char_stats:
            if char_stats[stat_type] == 0:
                print(f"{stat_type}?".title(), end=" ")
        empty_line()
        stat_type = clean_input("I want to increase my: ")
        terminal_spaces()

        # type for str strength, dex dexterity, etc.
        if stat_type in char_stats:
            if char_stats[stat_type] == 0:
                char_stats[stat_type] += stats_to_assign[i_stats_to_assign]
                i_stats_to_assign += 1
            elif stat_type in char_stats:
                print(f"{name}, you have already assigned that stat! Pick another")
        else:
            print("That's invalid... Try an actual stat!")

    get_hp()

    print("You have chosen the following stat allotments!")
    for stat, points in char_stats.items():
        print(stat.title(), ": ", points, sep="")

    # add an "are you sure this is what you want"
    # redo from beginning or current roll?

    export_character(char_stats)


def rolling_start_stats():
    while True:
        stats_to_pick = getting_stats()
        average_of_stats = sum(stats_to_pick) / len(stats_to_pick)
        percentage_allocation = (average_of_stats / 18) * 100

        while True:
            print("Here are the stats you rolled:")
            for stat_value in stats_to_pick[:-1]:
                print(stat_value, sep="", end=", ")
            print(stats_to_pick[-1], ".", sep="")

            print("Your average stat allocation is...")
            print(f"*{average_of_stats:.2f} out of 18*")
            print(f"That is a {percentage_allocation:.02f}% allocation rate!")
            # eventually ifs for percentage so it says if good or bad etc
            print("Would you like to re-roll your stats?")

            re_roll = clean_input("(Y)es/(N)o: ")
            if re_roll in no_variants:
                terminal_spaces()
                return stats_to_pick
            elif re_roll == "yes" or re_roll == "y":
                terminal_spaces()
                break
            else:
                empty_line()
                print("Well... That wasn't a (y)es or a (n)o...")
                print("I could be mean, and force you to re-roll, but you can try again :)")
                empty_line()


def getting_stats():
    stats_needed = 6
    stats_to_pick = []
    while stats_needed > 0:
        total = roll_character_stats()
        stats_to_pick.append(total)
        stats_needed -= 1
    return stats_to_pick


def roll_character_stats():
    max_rolls = 4
    possible_values = []
    while max_rolls > 0:
        rolled_number = d6_roll()
        possible_values.append(rolled_number)
        max_rolls -= 1
    possible_values.remove(min(possible_values))
    total = sum(possible_values)
    return total


def export_character(character_stats, filename="character_stats.txt"):
    with open(filename, 'w') as file:
        for stat, value in character_stats.items():
            file.write(f"{stat}: {value}\n")


def get_name_role():
    char_stats["name"] = input("What is your name?: ").title()
    char_stats["class"] = input("What class would you like to be?: ").title()


def get_hp():
    con = char_stats['constitution']
    con_mod = modifier.get_modifier(con)
    class_hp_dice = 12
    hp = con_mod + class_hp_dice
    char_stats['hp'] = hp
