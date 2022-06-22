
from model.player import Player
from model.weapon import weapon

sword = weapon("épee", 3)
player1 = Player("fati", 20, 3)

player1.set_weapon(sword)
player2 = Player("toto", 20, 3)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())

print("bienvenu à ", player1.get_pseudo(), "/", "vos hp sont de ", player1.get_health(), "/", "votre attaque est de ", player1.get_attack_value())
print("bienvenu à ", player2.get_pseudo(), "/", "vos hp sont de ", player2.get_health(), "/", "votre attaque est de ", player2.get_attack_value())

