from hero import Hero
from monster import Monster

def choose_action():
    action = input("Choose your action (attack/level_up/heal/defend): ").lower()
    return action


def game():
    hero_name = input("Enter your hero's name: ")
    hero = Hero(hero_name)
    monster = Monster("scary", hero.level)

    while hero.hp > 0:
        print(f"\n{hero.hero_name}'s Level {hero.level}, HP: {hero.hp}, Damage: {hero.damage} Coins: {hero.coins}")
        print(f"{monster.monster_name}'s Level: {monster.level}, HP: {monster.hp}, Damage: {monster.damage}")
        action = choose_action()
        if action == "attack":
            hero.attack(monster)
        elif action == "level_up":
            hero.level_up()
        elif action == "heal":
            hero.heal()
        elif action == "defend":
            hero.defend()
        if monster.hp <= 0:
            print(f"{monster.monster_name} is defeated! creating a new one.")
            monster = Monster("another_monster", hero.level)
        monster.attack(hero)
        if hero.hp <= 0:
            print(f"{hero.hero_name} is defeated! Game over.")
            break

if __name__ == "__main__":
    game()


       

        

        







