family = {
    "Grandfather": ["Father", "Uncle"],
    "Father": ["Ali", "Ahmed"],
    "Uncle": ["Sara"],
    "Ali": [],
    "Ahmed": [],
    "Sara": []
}

def dfs(person):
    for child in family[person]:
        print(child)
        dfs(child)

dfs("Grandfather")