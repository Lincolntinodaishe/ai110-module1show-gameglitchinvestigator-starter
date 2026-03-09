

def most_endangered(species_list):
    return sorted(species_list, key=lambda d: d["population"])[0]['name']

species_list = [
    {"name": "Naman",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    },
    {"name" : "Amur Leopard",
     "habitat" : "London",
     "population": 4

    }
]

print(most_endangered(species_list))
from collections import Counter
def max_species_copies(raised_species, target_species):
    list1 = []
    dict1 = {}
    #dict1 = Counter(set(raised_species))
    for i in raised_species:
       dict1[i] = dict1.get(i, 0)+1
    for i in target_species:
        list1.append(dict1[i])
    return min(list1)


raised_species1 = "abcba"
target_species1 = "abc"
print(max_species_copies(raised_species1, target_species1))  # Output: 1

raised_species2 = "aaaaabbbbcc"
target_species2 = "abc"
print(max_species_copies(raised_species2, target_species2)) # Output: 2

def count_unique_species(ecosystem_data):
    
    





