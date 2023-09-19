import random
class Monster:
    K_PROPORTION = 1.5  
    def __init__(self, monster_name, hero_level):
        self.monster_name = monster_name
        self.level = hero_level + random.randint(-1, 1)  
        self.hp = int(self.level * self.K_PROPORTION)  
        self.damage = int(self.level * self.K_PROPORTION)  

    def attack(self, hero):
        hero.reduce_health(self)

    def reduce_health(self, hero):
        self.hp -= hero.damage
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def __repr__(self):
        return f"Monster Name: {self.monster_name}, Level: {self.level}, HP: {self.hp}, Damage: {self.damage}"