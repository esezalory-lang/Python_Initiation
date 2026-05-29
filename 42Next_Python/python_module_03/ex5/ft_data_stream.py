#!/bin/python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["bowie", "jagger", "dylan", "hendrix", "mercury"]
    actions = ["duck walk", "hip shuffle", "windmill", "frog jump",
               "axe kick", "good foot", "splits", "moonwalk"]
    player = random.choice(players)
    move = random.choice(actions)
    yield player, move


def consume_event(full_events: list) -> typing.Generator[list, None, None]:
    single_event = random.choice(full_events)
    print(f"Got event from list: {single_event}")
    full_events.remove(single_event)
    yield full_events


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        rocknroll = next(gen_event())
        print(f"Event {i}: Player {rocknroll[0]} did action {rocknroll[1]}")
    events = []
    for i in range(10):
        events += [next(gen_event())]
    print(f"Built list of 10 events: {events}")
    for i in range(10, 0, -1):
        events = next(consume_event(events))
        print(f"Remains in list: {events}")
