import time

from models import Profile
import secrets


def final_touch():
    return (time.time_ns() % 123) + secrets.randbelow(15)


def match(p1: Profile, p2: Profile) -> float:
    return abs(p1.gender - p2.gender) * abs(p1.age - p2.age) + final_touch() + abs(p1.user_id - p2.user_id) * \
            len(f"8{'='*secrets.randbelow(1000)}>") + len(f"800{'0' * secrets.randbelow(300)}85")

