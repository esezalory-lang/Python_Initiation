#!/bin/python3

import sys


class ScoreError(Exception):
    def __init__(self: "ScoreError", message: str = "Unknown") -> None:
        super().__init__(message)


def analyse_stats(scores: list) -> None:
    n_players = int(len(scores))
    total = int(sum(scores))
    print(f"Total players: {n_players}")
    print(f"Total score: {total}")
    print(f"Average score: {(total/n_players):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


def record_player_stats() -> None:
    score_list = []
    try:
        for i in sys.argv[1::]:
            try:
                score = int(i)
                if score < 0:
                    raise ValueError
                score_list += [score]
            except ValueError:
                print(f"Invalid parameter: '{i}'")
        if len(score_list) == 0:
            raise ScoreError(f"python3 {sys.argv[0]} <score1> <score1> ...")
        else:
            print(f"Scores processed: {score_list}")
            analyse_stats(score_list)
    except ScoreError as s:
        print(f"No scores provided. Usage: {s}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    record_player_stats()
