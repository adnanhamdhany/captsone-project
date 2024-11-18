import random

responses_freshness = [
    {
        "Tingkat Kesegaran": "Segar"
    },
    {
        "Tingkat Kesegaran": "Tidak Segar"
    }
]

def get_random_freshness():
    return random.choice(responses_freshness)