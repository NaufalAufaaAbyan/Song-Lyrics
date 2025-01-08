import time
import sys

def print_lyrics():
    lines = [
        ("So I'ma love you every night like it's the last night", 0.1),
        ("Like it's the last night", 0.1),
        ("If the world was ending, I'd wanna be next to you", 0.1),
        ("If the party was over and our time on Earth was through", 0.1),
        ("I'd wanna hold you just for a while and die with a smile", 0.1),
        ("If the world was ending, I'd wanna be next to you", 0.1),
        ("Right next to you", 0.1)
    ]

    delays = [0.5, 0.5, 1.10, 1.25, 1.5, 2.0, 1.0]

    line_delays = delays[:len(lines)]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(char_delay)
        print('')
        time.sleep(line_delays[i])

print_lyrics()