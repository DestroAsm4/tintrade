from Tools import tool_to_ruble, buy
from SETTING import TOKEN
from figi import FIGI
import asyncio
from algotacts import T1
import threading

tmos = T1('tmos')
# tbru = T1('trur')

# init events

tmos.loop_buy()

# e1 = threading.Event()
# e2 = threading.Event()
# tmos.loop_buy()
# init threads
# t1 = threading.Thread(target=tmos.loop_buy)
# t1 = threading.Thread(target=tmos.loop_sell, args=(6.41,))
# t2 = threading.Thread(target=tbru.loop_buy)

# start threads






# def main():
#     t1.start()
#     # t2.start()
#
#     e1.set()  # initiate the first event
#
#     # join threads to the main thread
#     t1.join()
#     # t2.join()
#
#
#
# if __name__ == "__main__":
#     main()



