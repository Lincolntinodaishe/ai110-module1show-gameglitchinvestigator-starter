

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

def is_valid_post_format(posts):
    d = {  ')' : "(",
            '}' : '{',
            ']' : '['
    }
    stack = []
    for i in posts:
        if i in '({[':
            stack.append(i)
        if i in ')}]':
            if stack and d[i] != stack[-1]:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    return False

print (is_valid_post_format("()"))
print (is_valid_post_format("()[]{}")) 
print (is_valid_post_format("(]"))


def is_symmetrical_title(title):
    l = 0
    r = len(title)-1
    title = title.lower()
    while l < r:
        if not title[l].isalpha() :
            l +=1
            continue
        if not title[r].isalpha():
            r -= 1
            continue
        if title[l] != title[r]:
            return False
        l += 1
        r -= 1
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

    
    





