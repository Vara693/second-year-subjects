import random
import time

WINDOW_SIZE = 4
TOTAL_FRAMES = 10
LOSS_PROB = 0.3

def selective_repeat():
    base = 0
    received = [False] * TOTAL_FRAMES

    while base < TOTAL_FRAMES:
        for i in range(base, min(base + WINDOW_SIZE, TOTAL_FRAMES)):
            if not received[i]:
                print(f"Sending Frame {i}")

        for i in range(base, min(base + WINDOW_SIZE, TOTAL_FRAMES)):
            if not received[i]:
                if random.random() < LOSS_PROB:
                    print(f"Frame {i} lost")
                else:
                    print(f"Frame {i} received → ACK sent")
                    received[i] = True

        while base < TOTAL_FRAMES and received[base]:
            base += 1

        time.sleep(1)

print("\n---- Selective Repeat Simulation ----")
selective_repeat()