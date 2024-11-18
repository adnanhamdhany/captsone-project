import random

responses_fish = [
    {
        "Jenis Ikan": "Ikan Lele"
    },
    {
        "Jenis Ikan": "Ikan Tuna"
    },
    {
        "Jenis Ikan": "Ikan Salmon"
    }
]

def get_random_fish():
    return random.choice(responses_fish)