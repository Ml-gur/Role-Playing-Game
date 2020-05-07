import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[1;36;255m'
    OKGREEN = '\033[1;32;255m'
    CARNING = '\033[93m'
    FAIL = '\033[1;31;255m'
    ENDC = '\033[0;0;255m'
#   BOLD = '\033[1m'
#   UNDERLINE = '\033[4m'
    

    

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
    
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def heal(self, dmg):
        self.hp += dmg
        if self.hp < self.maxhp:
           self.hp = self.maxhp

    
    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, cost):
        self.mp -= cost
        
    
    def choose_action(self):
        i = 1
        print('\n' + '---------' + self.name + '---------')
        print(bcolors.OKBLUE + ' ACTIONS:' + bcolors.ENDC)
        for item in self.actions:
            print('    ' + str(i) + '.', item)
            i += 1
            
    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + '\n\n   MAGIC:' + bcolors.ENDC)
        for spell in self.magic:
            print('      '+ str(i) + '.', spell.name, '(cost:', str(spell.cost) + ' MP)')
            i += 1
            
    def choose_item(self):
        i = 1
        print(bcolors.OKBLUE + '\n\n   ITEMS:' + bcolors.ENDC)
        for item in self.items:
            print('      '+ str(i) + '.', item['item'].name + ':', item['item'].description, 
                  '(x' + str(item['quantity']) + ')')
            i += 1   
    
    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + " TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() !=0:
                print("       " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("Choose target: ")) - 1
        return choice
            
    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, 3)
        spell = self.magic[magic_choice]
        pct = (self.hp / self.maxhp) * 100        
        while spell.magic_type == "White" and pct > 50:
            magic_choice = random.randrange(0, 3)
            spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        return spell, magic_dmg
    
    
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2
            
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
            
        while len(hp_bar) < 50:
            hp_bar += " "

#Add space for hp bar        
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        
        if len(hp_string) < 11:
            decreased_hp = 11 - len(hp_string)      
            
            while decreased_hp > 0:
                current_hp += " "
                decreased_hp -= 1
            
            current_hp += hp_string
            
        else:
            current_hp = hp_string

            
#Print bars            
        print('                         __________________________________________________')
        print(self.name + '       ' + str(current_hp) + ' |' + bcolors.FAIL 
              + hp_bar + bcolors.ENDC + '|')
    
    
    
    
    
    def get_stats(self):
#Add █ for mp and hp
        hp_bar= ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4
        
        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10
        
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        
        while len(hp_bar) < 25:
            hp_bar += " "
        
        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
            
        while len(mp_bar) < 10:
            mp_bar += " "


#Add space for hp bar        
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        
        if len(hp_string) < len(str(self.maxhp) + "/" + str(self.maxhp)):
            decreased_hp = len(str(self.maxhp) + "/" + str(self.maxhp)) - len(hp_string)      
            
            while decreased_hp > 0:
                current_hp += " "
                decreased_hp -= 1
            
            current_hp += hp_string
            
        else:
            current_hp = hp_string


#Add space for mp bar
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""
        
        if len(mp_string) < len(str(self.maxmp) + "/" + str(self.maxmp)):
            decreased_mp = len(str(self.maxmp) + "/" + str(self.maxmp)) - len(mp_string)      
            
            while decreased_mp > 0:
                current_mp += " "
                decreased_mp -= 1
            
            current_mp += mp_string
            
        else:
            current_mp = mp_string


 #Print bars            
        print('                         _________________________             __________')
        print(self.name + '         ' + str(current_hp) + ' |' + bcolors.OKGREEN 
              + hp_bar + bcolors.ENDC 
              + '|   ' + str(current_mp) + ' |' + bcolors.OKBLUE + mp_bar 
              + bcolors.ENDC + '|')

