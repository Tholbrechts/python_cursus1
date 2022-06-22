class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("bienvenu à ", pseudo, "/", "vos hp sont de ", health, "/", "votre attaque est de ", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.attack)


class Warrior(Player):
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.armor = 3
        print("bienvenu au guerrier ", pseudo, "/", "vos hp sont de ", health, "/", "votre attaque est de ", attack)

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage)


    def blade(self):
        self.armor = 3

    def get_armor_point(self):
        return self.armor


player = Player("toto", 20, 2)
player.damage(3)

warrior = Warrior("DarkWarrior", 30, 4)

warrior.damage(4)
print(warrior.get_health(), warrior.get_armor_point())
warrior.damage(4)
print(warrior.get_health(), warrior.get_armor_point())
warrior.damage(4)
print(warrior.get_health(), warrior.get_armor_point())
warrior.damage(4)
print(warrior.get_health(), warrior.get_armor_point())


if issubclass(Warrior, Player):
    print('ok')
