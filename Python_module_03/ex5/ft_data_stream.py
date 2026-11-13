import random
import typing

names_list = [
    "bob",
    "alice",
    "dylan",
    "charlie",
]

actions_list = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
]


def gen_event() -> typing.Generator:
    while True:
        name = random.choice(names_list)
        action = random.choice(actions_list)
        yield (name, action)


def consume_event(lst: list) -> typing.Generator:
    while lst:
        removed_element = random.choice(lst)
        lst.remove(removed_element)
        yield removed_element


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()
    for i in range(1000):
        output = next(event_gen)
        print(f"Event {i}: Player {output[0]} did action {output[1]}")

    event_gen2 = gen_event()
    ten_list = []
    for x in range(10):
        ten_list.append(next(event_gen2))
    print(f"Built list of 10 events: {ten_list}")

    for event in consume_event(ten_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_list}")
