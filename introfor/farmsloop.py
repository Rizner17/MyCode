#!/usr/bin/env python3

"""AJRodriguez | Lab 23c: farm loop creation"""

#create a list of farms
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

##print(farms[2]) <-----i know this works

for x in farms:
    print("\nThe ", + (print(farms[x].get("name"))), " is for ", (print(farms[x].get("agriculture"))))
