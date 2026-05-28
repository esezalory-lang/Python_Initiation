#!/bin/python3

import random


def gen_player_achievement() -> set:
    achievements = ["Sharpshooter", "In It To Win It", "Spree Master",
                    "Domination", "Battle Hardened", "Killionaire",
                    "Untouchable", "Steady Aim", "Tempered Blade",
                    "Scavenger Hunt", "Kilimanjaro", "The One Percent",
                    "Checkmate", "I Dabble in Slaying", "No Pain, No Gain"]
    n_achievements = len(achievements)
    spartan = set(random.choices(achievements, weights=None, cum_weights=None,
                                 k=random.randint(1, n_achievements)))
    return spartan


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    Alice = gen_player_achievement()
    Bob = gen_player_achievement()
    Charlie = gen_player_achievement()
    Dylan = gen_player_achievement()

    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}\n")

    commonality = Alice.union(Bob, Charlie, Dylan)
    print(f"All distinct achievements: {commonality}\n")

    print("Common achievements:",
          f"{commonality.intersection(Alice, Bob, Charlie, Dylan)}\n")

    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Alice, Bob, Dylan)}")
    print(f"Only Dylan has: {Charlie.difference(Alice, Bob, Charlie)}\n")

    print(f"Alice is missing: {commonality.difference(Alice)}")
    print(f"Bob is missing: {commonality.difference(Bob)}")
    print(f"Charlie is missing: {commonality.difference(Charlie)}")
    print(f"Dylan is missing: {commonality.difference(Dylan)}")
