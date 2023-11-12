from __future__ import annotations
from random import randint


class Unit():
    # assigning ID variable
    index_number = 0

    def __init__(self, team) -> None:
        # after initialising object of a class would have own id
        Unit.index_number += 1
        self.id = Unit.index_number
        self.team = team


class Soldier(Unit):
    def __init__(self, team) -> None:
        # as class attribute Soldier class initialiser not taking team number
        # but parent class Unit can take
        super().__init__(team)
        # by default soldier has no hero to follow
        self.my_hero = None
        self.team = team

    # taking an object of Hero class
    def follow(self, obj: Hero):
        # assigning it ID as attribute of Soldier class
        self.my_hero = obj.id
        print(f'+++ Soldier {self.id} from team {self.team} '
              f'following the Hero {obj.id} +++')


class Hero(Unit):
    def __init__(self, team) -> None:
        # inheriting class Unit initialiser give us opportunity
        # to use id attribute
        super().__init__(team)
        self.level = 1
        self.team = team

    def level_up(self):
        self.level += 1
        print(f'Hero from team {self.team} got level up - {self.level}!')
        print('-----------------------------------')


# creating heroes for our teams
Hero_1 = Hero(1)
Hero_2 = Hero(2)

print('===================================')


def add_army():
    # creating lists of soldiers
    army_1 = []
    army_2 = []
    # soldier count for each army would be random
    army_count = randint(1, 10)
    print(f'{army_count} soldiers from team has been spawned')
    for i in range(army_count):
        # soldiers will chose random team
        team_choice = randint(1, 2)
        if team_choice == 1:
            # creating object of Soldier class and append this object to a list
            army_1.append(Soldier(team_choice))
        else:
            army_2.append(Soldier(team_choice))
    print(f'Team 1 army count is equals {len(army_1)}')
    print(f'Team 2 army count is equals {len(army_2)}')
    if len(army_1) > len(army_2):
        Hero_1.level_up()
    elif len(army_2) > len(army_1):
        Hero_2.level_up()
    else:
        print('Armies of both teams equals!')
    if len(army_1) > 0:
        if army_1[0] is not None:
            # ordering soldier from first team to follow first hero
            army_1[0].follow(Hero_1)
        else:
            print('Ahtung!')
    print('-----------------------------------')
    # resetting armies after end of the loop
    # for correct work of multiple add_army function call
    army_1 = None
    army_2 = None


print('How much rounds in a game you want?')
rounds_count = int(input())
print('-----------------------------------')
round_number = 0

for i in range(rounds_count):
    round_number += 1
    print(f'Round {round_number} started!')
    add_army()

if Hero_1.level > Hero_2.level:
    print('*** Team 1 wins! ***')
elif Hero_2.level > Hero_1.level:
    print('*** Team 2 wins! ***')
elif Hero_2.level == Hero_1.level:
    print('*** Tie! ***')

print('===================================')
