"""
fait par: Vincent Brouillet
groupe: 405
exercice 1 du TP4
"""

import math
import random as r
from dataclasses import dataclass

projet = int(input("quelle projet voulez-vous voir?"))

# met un message en majuscule
if projet == 1:
    class StringFoo:

        def __init__(self):
            self.message = ""

        def set_string(self):
            self.message = message

        def print_string(self):
            self.message = message.upper()
            print(f"{self.message}")

    message = input(f"Quelle est votre message?")
    StringFoo().set_string()
    StringFoo().print_string()

# calcul l'aire d'un rectangle
elif projet == 2:
    class rectangle:
        def __init__(self):
            self.largeur = int(input(f"largeur?"))
            self.longueur = int(input(f"longeur?"))
            self.aire = None

        def calcul_aire(self):
            self.aire = self.largeur * self.longueur

        def afficher_infos(self):
            print(f"largeur: {self.largeur} \nlongueur: {self.longueur} \nAire: {self.aire}")

    rectangle().calcul_aire()
    rectangle().afficher_infos()

# calcul l'aire et la circonférance d'un cercle
elif projet == 3:
    class Cercle:
        def __init__(self):
            self.rayon = int(input(f"rayon?"))
            self.aire = None
            self.circ = None

        def calcul_aire(self):
            self.aire = math.pi*self.rayon**2

        def calcul_circonference(self):
            self.circ = 2*math.pi*self.rayon

        def afficher_infos(self):
            print(f"rayon: {self.rayon} \naire: {self.aire} \ncirconference: {self.circ}")

    Cercle().calcul_aire()
    Cercle().calcul_circonference()
    Cercle().afficher_infos()

# simule les stat d'un hero
elif projet == 4:
    class Hero:
        def __init__(self):
            self.point_de_vie = r.randint(1, 10) + r.randint(1, 10)
            self.attack = r.randint(1, 6)
            self.defense = r.randint(1, 6)
            self.nom = input(f"nom?")
            self.vivant = True
            self.attack_total = None

        def faire_attack(self):
            self.attack_total = self.attack + r.randint(1, 6)
            print(f"{self.attack_total} dmg")

        def recevoir_dommages(self, mdmg):
            self.point_de_vie -= mdmg - self.defense
            print(self.point_de_vie)
            if self.point_de_vie <= 0:
                self.vivant = False

        def est_vivant(self):
            print(f"vivant: {self.vivant}")

        def afficher_infos(self):
            print(f"vie: {self.point_de_vie}\nattack: {self.attack}\ndefense: {self.defense}\nnom: {self.nom}")

    Hero().afficher_infos()
    Hero().faire_attack()
    Hero().recevoir_dommages(5)
    Hero().est_vivant()

# simule un personnage de dnd
elif projet == 5:
    @dataclass
    class dnd:
        force: 0
        dexterite: 0
        constitution: 0
        intelligence: 0
        sagesse: 0
        charisme: 0

        def afficher_infos(self):
            print(f"force: {self.force} \ndexterrite: {self.dexterite} \nconstitution: {self.constitution}"
                  f" \nintelligence: {self.intelligence} \nsagesse: {self.sagesse} \ncharisme: {self.charisme}")

    dnd(r.randint(1, 20), r.randint(1, 20), r.randint(1, 20),
        r.randint(1, 20), r.randint(1, 20), r.randint(1, 20)).afficher_infos()

# mélange du projet 4 et 5
elif projet == 6:
    @dataclass
    class HeroData:
        force: int
        dexterite: int
        constitution: int
        intelligence: int
        sagesse: int
        charisme: int


    class HeroDnd:
        def __init__(self):
            self.data = HeroData(r.randint(1, 20), r.randint(1, 20), r.randint(1, 20),
                                 r.randint(1, 20), r.randint(1, 20), r.randint(1, 20))

        def afficher_infos(self):
            print(f"force: {self.data.force} \ndexterité: {self.data.dexterite}"
                  f" \nconstitution: {self.data.constitution} \nintelligence: {self.data.intelligence}"
                  f" \nsagesse: {self.data.sagesse} \ncharisme: {self.data.charisme} \n")

        def dice_roll(self):
            choix = int(input("stat: \n1-force \n2-dexterité \n3-constitution"
                              " \n4-intelligence \n5-sagesse \n6-charisme"))
            if choix == 1:
                print(f"you rolled  a {self.data.force + r.randint(1, 6)} in force")
            elif choix == 2:
                print(f"you rolled  a {self.data.dexterite + r.randint(1, 6)} in dexterité")
            elif choix == 3:
                print(f"you rolled  a {self.data.constitution + r.randint(1, 6)} in constitution")
            elif choix == 4:
                print(f"you rolled  a {self.data.intelligence + r.randint(1, 6)} in intelligence")
            elif choix == 5:
                print(f"you rolled  a {self.data.sagesse + r.randint(1, 6)} in sagesse")
            elif choix == 6:
                print(f"you rolled  a {self.data.charisme + r.randint(1, 6)} in charisme")


    hero = HeroDnd()
    hero.afficher_infos()
    hero.dice_roll()
