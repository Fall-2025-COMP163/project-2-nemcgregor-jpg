"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Noble McGregor
Date: 11/11/25

AI Usage: AI helped me in this project on understanding concepts such as super(), AI also allowed the great and formatted creation of the read me
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================
import random

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):      
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = None
        
        pass
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        damage = self.strength + self.magic 
        if self.weapon:
            damage += self.weapon.damage_bonus
        
        print(f"{self.name} attacked {target.name}, {self.name} did {damage} to target!")  
        target.take_damage(damage)
        pass
        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        self.health -= damage
        print(f"{self.name} took {damage} damage, your health is {self.health}")
        if self.health <= 0:
            self.health = 0
            print(f"You died!")
        pass
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"{self.name}'s stats --->")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")
        pass

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        pass
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        super().display_stats()
        print(f"{self.name}'s stats --->")
        print(f"{self.name}'s class is: {self.character_class}")
        print(f"{self.name}'s strength is: {self.strength}")
        print(f"{self.name}'s health is: {self.health}")
        print(f"{self.name}'s magic is: {self.magic}")
        print(f"{self.name}'s level is: {self.level}")
        print(f"{self.name} has {self.experience} experience points.")
        pass

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        super().__init__(name, character_class = "Warrior", health = 200, strength = 15, magic = 5)
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        super().attack(target)
        physical_bonus = 5
        print(f"{self.name} does extra physical damage for {physical_bonus} damage!")
        total_damage = self.strength + self.magic + physical_bonus
        target.take_damage(total_damage)
        pass
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        special_damage = (self.strength * 3) + self.magic
        print(f"{self.name} used Power Strike! It did {special_damage} damage!")
        target.take_damage(special_damage)
        pass

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        super().__init__(name, character_class = "Mage", health = 150, strength = 5, magic = 15)
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        super().attack(target)
        magical_bonus = 10
        print(f"{self.name} does extra magical damage for {magical_bonus} damage!")
        total_damage = self.strength + self.magic + magical_bonus
        target.take_damage(total_damage)
        pass
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        special_damage = (self.magic * 2) + self.magic + self.strength
        print(f"{self.name} used Fireball! It did {special_damage} damage!")
        target.take_damage(special_damage)
        pass


class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        super().__init__(name, character_class = "Rogue", health = 175, strength = 5, magic = 5)
        pass
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """ 
        super().attack(target)

        stealth_bonus = 15
        print(f"{self.name} does extra physical damage for {stealth_bonus} damage!")
        critical = random.randint(1, 10)
        if critical >= 5:
            critical = 15
            print(f"{self.name} landed a critical hit! they dealt {critical} extra damage!")
            total_damage = self.strength + self.magic + stealth_bonus + critical
            target.take_damage(total_damage)
        else:
            total_damage = self.strength + self.magic + stealth_bonus    
            target.take_damage(total_damage)
        pass
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        critical = random.randint(1, 10)
        special_damage = (self.strength + self.magic) * (critical)
        print(f"{self.name} used Sneak Attack! It did {special_damage} damage!")
        target.take_damage(special_damage)
        pass

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        self.name = name
        self.damage_bonus = damage_bonus
        pass
        
    def display_info(self):
        """
        Display information about this weapon.
        """

        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}")
        pass
        
    

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  
    
    
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
     
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
     
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
