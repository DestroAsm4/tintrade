from tinkoff.invest import Client, RequestError, OrderDirection, OrderType, Quotation
from datetime import datetime
import asyncio
import time
from SETTING import TOKEN
from figi import FIGI
from datetime import timedelta
from tinkoff.invest import CandleInterval, Client, Quotation, LastPrice
from tinkoff.invest.utils import now


class Tool:

    def __init__(self, figi_name):
        self.TOKEN = TOKEN
        self.FIGI = FIGI[figi_name]
        self.ACCID = self.accid()



    def price_to_float(self, prise):
        '''

        :param prise: Quotation, LastPrice...
        :return:
        '''
        return float(prise.units + prise.nano / 1000000000)







    # def cup_dict(self, bid_ask: dict):
    #     bid_ask[]





    def moving_average(self, period = 10):
        HOUR = 10
        HALF_HOUR = 5
        mov_avr = []

        data_by_5_min = self.avg_tool_hour()
        count_data = len(data_by_5_min)
        del_data = count_data % period
        del data_by_5_min[:del_data]
        iter = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
        iter(data_by_5_min, period)
        res = [round(sum(i)/len(i), 2) for i in iter(data_by_5_min, period)]
        return res



    def avg_tool_hour(self):

        close_data = []
        with Client(self.TOKEN) as client:
            for candle in client.get_all_candles(
                figi=self.FIGI,
                from_=now() - timedelta(days=30),
                interval=CandleInterval.CANDLE_INTERVAL_5_MIN,
            ):
                candle_to_day = {
                    "open": float(f'{str(candle.open.units)}.{str(candle.open.nano)[:2]}'),
                    "high": float(f'{str(candle.high.units)}.{str(candle.high.nano)[:2]}'),
                    "low": float(f'{str(candle.low.units)}.{str(candle.low.nano)[:2]}'),
                    "close": float(f'{str(candle.close.units)}.{str(candle.close.nano)[:2]}'),
                    "time": f'{candle.time.time().hour}:{candle.time.time().minute}'

                }
                close_data.append(candle_to_day["close"])
            return close_data



    def singl_tool(self, type_req: str = 'tool_rubl'):
        '''

        :param TOKEN:
        :param FIGI: in file figi.py
        :param type_req: tool_rubl or bid_ask
        :return:
        '''
        with Client(self.TOKEN) as client:
            time.sleep(1)
            tool = client.market_data.get_order_book(figi=self.FIGI, depth=20)
            last_price = self.price_to_float(tool.last_price)
            tool = {
                    'tool_rubl': last_price,
                    'bid_ask': {
                        'bid': tool.bids,
                        'ask': tool.asks
                        }
                    }
            return tool[type_req]

    async def asinc_singl_tool(self):
        for i in range(3):
            print(self.singl_tool())




    def buy(self):
        try:
            with Client(self.TOKEN) as client:

                result = client.orders.post_order(
                    order_id=str(datetime.utcnow().timestamp()),
                    figi=FIGI,
                    quantity=1,
                    account_id=self.ACCID,
                    direction=OrderDirection.ORDER_DIRECTION_BUY,
                    order_type=OrderType.ORDER_TYPE_MARKET
                )
                return result

        except RequestError as e:
            print(str(e))

    def sell(self):
        try:
            with Client(self.TOKEN) as client:

                result = client.orders.post_order(
                    order_id=str(datetime.utcnow().timestamp()),
                    figi=FIGI,
                    quantity=1,
                    account_id=self.ACCID,
                    direction=OrderDirection.ORDER_DIRECTION_SELL,
                    order_type=OrderType.ORDER_TYPE_MARKET
                )
                return result

        except RequestError as e:
            print(str(e))

    def accid(self):
        with Client(self.TOKEN) as client:
            return client.users.get_accounts().accounts[0].id

# tool = Tool('CHMF')
# print(tool.singl_tool())



# print(moving_average(TOKEN, FIGI['tmos']))
# print(singl_tool_to_ruble(TOKEN, FIGI['tmos']))
# lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
# print(singl_tool(TOKEN, FIGI['tmos'], 'bid_ask')['bid'])