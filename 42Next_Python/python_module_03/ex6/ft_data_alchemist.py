#!/bin/python3

import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    legends = ["Dan", "chongwei", "Hartono", "hidayat",
               "Susanti", "lingwei", "Nehwal", "momota",
               "Yuqi", "Vitidsarn", "Popov", "Antonsen"]
    print(f"Initial list of players: {legends}")
    formatted = [name.capitalize() for name in legends]
    print(f"New list with all names capitalized: {formatted}")
    only_caps = [name for name in legends if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_caps}")
    legend_scores = {name: random.randint(50000, 100000) for name in only_caps}
    print(f"Score dict: {legend_scores}")
    average_score = round(sum(legend_scores.values())/len(legend_scores), 2)
    print(f"Score average is {average_score}")
    above_average = {name: scores for name, scores in legend_scores.items()
                     if scores > average_score}
    print(f"High scores: {above_average}")
