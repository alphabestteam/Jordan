class Hero:
    M = 1.5
    K = 5

    def __init__(self, hero_name):
        self.hero_name = hero_name
        self.hp = 10
        self.damage = 2
        self.level = 1
        self.coins = 0
        self.is_defending = False
    
    def heal(self):
        LIFE = (self.hp / 10) * 100
        return f'life: {LIFE}%'
    
    def level_up(self):
        cost_to_upgrade = self.K * (self.level + 1)
        if self.coins >= cost_to_upgrade:
            self.coins -= cost_to_upgrade
            self.level += 1
            self.damage *= self.M
            self.hp = 10
        else:
            print("Not enough coins to level up!")

    def attack(self, monster):
        monster.reduce_health(self)
    
    def defend(self):
        self.is_defending = True

    def reduce_health(self, monster):
        if self.is_defending:
            self.hp -= monster.damage * 0.2
        else:
            self.hp -= monster.damage
        if self.hp < 0:
            self.hp = 0
        self.is_defending = False
        return self.hp

    def increase_coins(self, coins_number):
        self.coins += coins_number
        
    def __repr__(self):
        return f"Hero Name: {self.hero_name}, Level: {self.level}, Damage: {self.damage}, Health: {self.hp}, Currency: {self.coins}"


    
