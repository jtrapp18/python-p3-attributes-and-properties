#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, name=None, breed=None):
        self.name = name
        self.breed = breed

        if name is None:
            pass
        elif isinstance(name, str) and (len(name) > 0) and (len(name) < 26):
            print(f"Setting name to {name}.")
        else:
            print("Name must be string between 1 and 25 characters.")

        if breed is None:
            pass
        elif breed in APPROVED_BREEDS:
            self.breed = breed            
        else:
            print("Breed must be in list of approved breeds.")

