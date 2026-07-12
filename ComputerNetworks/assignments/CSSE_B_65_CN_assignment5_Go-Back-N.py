import random
import time

WINDOW_SIZE = 4
TOTAL_FRAMES = 10
LOSS_PROB = 0.3

def go_back_n():
    base = 0
    next_seq = 0

    while base < TOTAL_FRAMES:
        while next_seq < base + WINDOW_SIZE and next_seq < TOTAL_FRAMES:
            print(f"Sending Frame {next_seq}")
            next_seq += 1

        for i in range(base, next_seq):
            if random.random() < LOSS_PROB:
                print(f"Frame {i} lost! Retransmitting from {i}")
                next_seq = i
                break
            else:
                print(f"ACK received for Frame {i}")
                base += 1

        time.sleep(1)

print("---- Go-Back-N Simulation ----")
go_back_n()