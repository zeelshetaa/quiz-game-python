import time


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time left: {i}s", end="\r")
        time.sleep(1)