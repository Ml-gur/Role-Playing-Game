from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


#Create Black Magic
fire = Spell("Fire", 10, 600, "Black")
thunder = Spell("Thunder", 10, 1600, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 1200, "Black")
quake = Spell("Quake", 14, 140, "Black")

#Create White Magic
cure = Spell("Cure", 25, 620, "White")
cura = Spell("Cura", 32, 1500, "White")


#Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 1000)

elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores HP/MP party's member", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


#Create inventory
player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, cure]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity":5},
                {"item": superpotion, "quantity":5}, {"item": elixer, "quantity":5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity":5}]


player1 = Person("Sam", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Bless", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Allan", 3089, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Kamonde", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Solo", 12000, 701, 525, 25, enemy_spells, [])
enemy3 = Person("Davie", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

defeated_enemies = 0
defeated_players = 0

#Game
running = True
i = 0


print(bcolors.FAIL + "\nENNEMIES ATTACK !" + bcolors.ENDC)

while True:
    try:
    
        while running:
            print("==================================================================================")
            print("NAME                     HP                                    MP")
        
            
            for player in players:
                player.get_stats()
            
            print("\n")        
            
            for enemy in enemies:
                enemy.get_enemy_stats()
            print("\n")
        
        #Players choice
            for player in players:    
                player.choose_action()
                index = int(input("Choose your action: ")) - 1

            
        #1 - Attack
                if index == 0:
                    dmg = player.generate_damage()
                    enemy = player.choose_target(enemies)
                    
                    enemies[enemy].take_damage(dmg)
                    print(bcolors.OKGREEN + "\nYou attacked " + enemies[enemy].name + " for",
                          dmg, "points of damage\n" + bcolors.ENDC)
                    
                    if enemies[enemy].get_hp() == 0:
                        print(bcolors.FAIL + enemies[enemy].name + " has died\n" + bcolors.ENDC)
                        defeated_enemies += 1 
                        del enemies[enemy]
                        if defeated_enemies == 3:
                            print(bcolors.OKGREEN + "\nYOU WIN!" + bcolors.ENDC)
                            running = False   
            
        #2 - Spells              
                elif index == 1:
                    player.choose_magic()
                    magic_choice = int(input("Choose magic: ")) - 1
                
                    if magic_choice == -1:
                        continue
                    
                    spell = player.magic[magic_choice]
                    magic_dmg = spell.generate_damage()
                    
                    current_mp = player.get_mp()
                
                    if spell.cost > current_mp:
                        print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                        continue
                   
                    player.reduce_mp(spell.cost)
                    
                    if spell.magic_type == "White":
                        player.heal(magic_dmg)
                        print(bcolors.OKBLUE + "\n" + spell.name + " heals for", 
                              str(magic_dmg), "HP\n" + bcolors.ENDC)
                        
                        
                    elif spell.magic_type == "Black":
                        enemy = player.choose_target(enemies)
                        enemies[enemy].take_damage(magic_dmg)
                        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                              "points of damage to " + enemies[enemy].name + "\n" + bcolors.ENDC)
                   
                    if enemies[enemy].get_hp() == 0:
                        print(bcolors.FAIL + enemies[enemy].name + " has died\n" + bcolors.ENDC)
                        defeated_enemies += 1 
                        del enemies[enemy]
                        if defeated_enemies == 3:
                            print(bcolors.OKGREEN + "\nYOU WIN!" + bcolors.ENDC)
                            running = False 
         
        #3 - Items       
                elif index == 2:
                    player.choose_item()
                    item_choice = int(input("Choose item: ")) - 1
                    
                    if item_choice == -1:
                        continue
                    
                    item = player.items[item_choice]["item"]
                    
                    if player.items[item_choice]["quantity"] == 0:
                        print(bcolors.FAIL + "\n" + "None left" + bcolors.ENDC)
                        continue
                        
                    player.items[item_choice]["quantity"] -= 1
                    
                    if item.item_type == "potion":
                        player.heal(item.prop)
                        print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop),
                              "HP\n" +bcolors.ENDC)
                    elif item.item_type == "elixer":
                        
                        if item.name == "MegaElixer":
                            for i in players:
                                i.hp = i.maxhp
                                i.mp = i.maxmp
                        else:        
                            player.hp = player.maxhp
                            player.mp = player.maxmp
                        print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP\n" + bcolors.ENDC)
                    elif item.item_type == "attack":
                        enemy = player.choose_target(enemies)
                        enemies.take_damage(item.prop)
                        print(bcolors.OKBLUE + "\n" + item.name + " deals", str(item.prop), "points of damage to " 
                              + enemies[enemy].name + "\n" + bcolors.ENDC)
                   
                    if enemies[enemy].get_hp() == 0:
                        print(bcolors.FAIL + enemies[enemy].name + " has died\n" + bcolors.ENDC)
                        defeated_enemies += 1 
                        del enemies[enemy]         
                        if defeated_enemies == 3:
                            print(bcolors.OKGREEN + "\nYOU WIN!" + bcolors.ENDC)
                            running = False
        
        #Enemies attack
                
            for enemy in enemies:
                if defeated_players == 2:
                        print(bcolors.FAIL + "\nYOU LOOSE, GAME OVER" + bcolors.ENDC)
                        running = False
                else:
                    enemy_choice = random.randrange(0, 2)
                    players_left = 3 - defeated_players
                    target = random.randrange(0, int(players_left))
             
              #1 - Attack      
                    if enemy_choice == 0:
                        enemy_dmg = enemies[0].generate_damage()
                        players[target].take_damage(enemy_dmg)
                        print(bcolors.FAIL + enemy.name + " attacks " + players[target].name 
                              + " for", str(enemy_dmg) + bcolors.ENDC)
                        if players[target].get_hp() == 0:
                            print(bcolors.FAIL + players[target].name + " has died" + bcolors.ENDC)
                            defeated_players += 1
                            del players[target]
                    
              #2 - Spells
                    elif enemy_choice == 1:
                        spell, magic_dmg = enemy.choose_enemy_spell()
                        if spell.magic_type == "Black": 
                            players[target].take_damage(magic_dmg)
                            print(bcolors.FAIL + enemy.name + " attacks " + players[target].name 
                                  + " for", str(magic_dmg) + " with " + str(spell.name) + bcolors.ENDC)
                            if players[target].get_hp() == 0:
                                print(bcolors.FAIL + players[target].name + " has died" + bcolors.ENDC)
                                defeated_players += 1
                                del players[target]
                                
                        elif spell.magic_type == "White": 
                            enemy.heal(magic_dmg)
                            print(bcolors.OKBLUE + enemy.name + " heals himself for", str(magic_dmg) 
                            + " with " + str(spell.name) + bcolors.ENDC)
                            
    except ValueError:
        print("Please choose between numbers given")
    except IndexError:
        print("Please choose between numbers given")
