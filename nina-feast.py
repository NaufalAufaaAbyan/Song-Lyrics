import sys
from time import sleep

def print_lyrics():
    lyrics = [
        ("aku tau kamu hebat", 0.05),
        ("namun selamanya diriku", 0.07),
        ("pasti berkutat", 0.09),
        ("tuk selalu jauhkanmu", 0.05),
        ("dari dunia yang jahat", 0.06),
        ("ini sumpahku padamu", 0.06),
        ("tuk biarkanmu", 0.06),
        ("tumbuh lebih baik", 0.13),
        ("cari panggilanmu", 0.09),
        ("jadi lebih baik", 0.1),
        ("dibanding diriku", 0.1),
        ("....", 0.1),
    ]

    pause = [1.1, 0.4, 1.7, 0.2, 1.5, 0.4, 0.5, 0.8, 0.8, 0.8, 0.8, 0.8]

    for i, (line, char_pause) in enumerate(lyrics):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_pause)
        print()
        sleep(pause[i])

print_lyrics()