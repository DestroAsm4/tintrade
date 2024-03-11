import asyncio
import os
from SETTING import TOKEN
# from tinkoff.invest import (
#     AsyncClient,
#     CandleInstrument,
#     MarketDataRequest,
#     SubscribeCandlesRequest,
#     SubscriptionAction,
#     SubscriptionInterval,
#     GetOrderBookRequest,
# )
# from figi import FIGI
#
#
# def get_cup():
#     GetOrderBookRequest(figi=FIGI['tbru'], depth=1)
#     # print(result)
#
# get_cup()

#
#
# async def main():
#     async def request_iterator():
#         yield MarketDataRequest(
#             subscribe_candles_request=SubscribeCandlesRequest(
#                 subscription_action=SubscriptionAction.SUBSCRIPTION_ACTION_SUBSCRIBE,
#                 instruments=[
#                     CandleInstrument(
#                         figi="BBG004730N88",
#                         interval=SubscriptionInterval.SUBSCRIPTION_INTERVAL_ONE_MINUTE,
#                     )
#                 ],
#             )
#         )
#         while True:
#             await asyncio.sleep(1)
#
#     async with AsyncClient(TOKEN) as client:
#         async for marketdata in client.market_data_stream.market_data_stream(
#             request_iterator()
#         ):
#             print(marketdata)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
from Tools import Tool

tool = Tool('CHMF')
#
#
# async def async_func():
#     print('Запуск ...')
#     await asyncio.sleep(1)
#     print('... Готово!')
#
#
# async def main():
#     f1 = asyncio.create_task (tool.asinc_singl_tool())
#     f2 = asyncio.create_task (async_func())
#     await f2
#     await f1
#
#
# asyncio.run(main())

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        tool.asinc_singl_tool())

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print (f"начато в {time.strftime('%X')}")

    # Подождите, пока не будут выполнены обе задачи (должно занять
    # около 2 секунд.)
    await task1
    print(f"функция 1 {time.strftime('%X')}")
    await task2

    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())


# import asyncio
# from codetiming import Timer
#
#
# async def task(name, work_queue):
#     timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
#     while not work_queue.empty():
#         delay = await work_queue.get()
#         print(f"Task {name} running")
#         timer.start()
#         await asyncio.sleep(delay)
#         timer.stop()
#
#
# async def main():
#     """
#     Это главная точка входа для главной программы
#     """
#     # Создание очереди работы
#     work_queue = asyncio.Queue()
#
#     # Помещение работы в очередь
#     for work in [15, 10, 5, 2]:
#         await work_queue.put(work)
#
#     # Запуск задач
#     with Timer(text="\nTotal elapsed time: {:.1f}"):
#         await asyncio.gather(
#             asyncio.create_task(task("One", work_queue)),
#             asyncio.create_task(task("Two", work_queue)),
#         )
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
