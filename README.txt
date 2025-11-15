
Character Abilities Showcase – COMP 163 Project 2

Author: Noble McGregor  
Date: 11/11/25  
Course: COMP 163  
Project Title: Character Abilities Showcase  
AI Usage: AI was used to understand object-oriented programming concepts such as `super()`, and to assist in formatting and writing this README.

Overview

This project demonstrates the use of object-oriented programming principles in Python through a fantasy-themed battle simulation. It showcases inheritance, polymorphism, and composition by implementing a hierarchy of character classes, each with unique attributes and behaviors. A provided battle engine is used to simulate combat between characters.

Class Structure

Character (Base Class)

The foundational class for all characters. It defines shared attributes and methods:

- Attributes: `name`, `health`, `strength`, `magic`, `weapon`
- Methods:
  - `attack(target)`: Calculates and applies damage based on strength and magic
  - `take_damage(damage)`: Reduces health, ensuring it does not fall below zero
  - `display_stats()`: Prints the character’s current stats

Player (Inherits from Character)

Adds player-specific features:

- Additional attributes: `character_class`, `level`, `experience`
- Overrides `display_stats()` to include class, level, and experience

Warrior, Mage, Rogue (Inherit from Player)

Each subclass defines its own stats and overrides the `attack()` method to reflect class-specific combat styles. Each also includes a unique special ability:

- Warrior:
  - High health and strength, low magic
  - `attack()`: Adds bonus physical damage
  - `power_strike(target)`: A powerful physical attack
- Mage:
  - Low health and strength, high magic
  - `attack()`: Emphasizes magic-based damage
  - `fireball(target)`: A high-damage magical spell
- Rogue:
  - Balanced stats
  - `attack()`: Includes a chance for a critical hit
  - `sneak_attack(target)`: Guaranteed critical hit with randomized multiplier

Weapon System

Weapon (Composition Class)

Implements a simple weapon system using composition. Characters can be equipped with a weapon that adds bonus damage to their attacks.

- Attributes: `name`, `damage_bonus`
- Method: `display_info()` prints weapon details

Weapons are assigned to characters by setting the `weapon` attribute:

warrior.weapon = Weapon("Iron Sword", 10)

Testing and Demonstration

The `main` block of the program demonstrates the following:

- Creation of Warrior, Mage, and Rogue characters
- Display of character stats
- Polymorphic behavior through overridden `attack()` methods
- Execution of each class’s special ability
- Weapon creation and assignment
- A full battle simulation using the `SimpleBattle` class

Concepts Demonstrated

- Inheritance: Shared behavior and attributes across character types
- Polymorphism: Overridden `attack()` methods for class-specific behavior
- Composition: Characters have weapons, modeled via the `Weapon` class
- Encapsulation: Each class manages its own data and behavior

How to Run

1. Ensure Python 3 is installed.
2. Save the code in a `.py` file.
3. Run the script using:


python character_showcase.py


4. Observe the output in the terminal, including character stats, attack behavior, and battle results.
