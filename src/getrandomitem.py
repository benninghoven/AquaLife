import random

def GetRandomItem(container):
    if isinstance(container, dict):
        random_key = random.choice(list(dic.keys()))
        random_value = dic[random_key]
        return random_value
    elif isinstance(container, list):
        return random.choice(container)

