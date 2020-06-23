import time
from tic_toc_timer import tic, toc, TicTocTimer

tic()
time.sleep(1)
print(f"The total time elasped is {toc()}")

tic("first")
time.sleep(10)
tic("second")
time.sleep(1)

first_elapsed = toc("first")  # expected ~ 11 secs
second_elapsed = toc("second")  # expected ~ 1 sec

timer = TicTocTimer()

timer.tic("first")
time.sleep(10)
timer.tic("second")
time.sleep(1)

first_elapsed = timer.toc("first")  # expected ~ 11 secs
second_elapsed = timer.toc("second")  # expected ~ 1 sec
