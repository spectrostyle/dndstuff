from character_creation import *
import csv


def main():
    terminal_spaces()
    header, monster = get_monster()
    weapon_name = monster[2]
    weapon = get_weapon(weapon_name)

    with open('character_stats.txt', 'r') as char_file:
        character_stats = char_file.readlines()

    if not character_stats:
        character_creator()

    header, monster = get_monster()
    weapon_name = monster[2]
    weapon = get_weapon(weapon_name)

    with open('character_stats.txt', 'r') as char_file:
        character_stats = char_file.readlines()

    for c, h, m in zip(character_stats, header, monster):
        print(c.strip().title(), end=" | ")
        if h == 'health':
            mon_con = int(monster[8])
            mod = modifier.get_modifier(mon_con)
            hp = get_health(m, mod)

            print(f"{h.title()}: {hp} mod({mod})")
        else:
            print(f"{h.title()}: {m.title()}")


def get_monster():
    with open('monsterstats.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        number_of_rows = sum(1 for _ in csv_reader)
        random_index = random.randint(1, number_of_rows)
        file.seek(0)
        for index, row in enumerate(csv_reader):
            if index == random_index:
                return header, row


def get_weapon(weapon_name):
    carried_weapons = []
    with open('items.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for weapon in weapon_name.split(','):
                if row[0] == weapon:
                    carried_weapons.append(row)
    return carried_weapons


def get_health(m, mod):
    hp = 0
    num_rolls, dice_face = m.split('d')
    num_rolls = int(num_rolls)
    dice_face = int(dice_face)

    if dice_face == 4:
        for _ in range(num_rolls):
            hp += d4_roll()
    if dice_face == 6:
        for _ in range(num_rolls):
            hp += d6_roll()
    if dice_face == 8:
        for _ in range(num_rolls):
            hp += d8_roll()

    hp += mod

    if hp == 0:
        hp += 1

    return hp


if __name__ == '__main__':
    main()
