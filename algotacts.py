from Tools import singl_tool, buy, sell, arg_tool_hour, moving_average
from SETTING import TOKEN
from figi import FIGI
import time

class T1:

    def __init__(self, figi_name):
        self.figi_name = figi_name
        self.point = 0.01
        self.perfect_price: float = 0
        self.avg_price_hour = moving_average(TOKEN, FIGI[self.figi_name])[-1]


    def loop_buy(self):

        print(self.avg_price_hour)
        while True:
            self.price = singl_tool(TOKEN, FIGI[self.figi_name], 'tool_rubl')
            if self.price <= self.avg_price_hour - self.mpoint(2):

                result = buy(TOKEN, FIGI[self.figi_name])
                self.price_buy = float(f'{str(result.initial_order_price.units)}.{str(result.initial_order_price.nano)[:2]}')
                print(self.price, self.avg_price_hour - self.mpoint(2))

                print(f"Количество лотов {str(result.lots_requested)}, цена покупки {str(result.initial_order_price.units)}.{str(result.initial_order_price.nano)[:2]}")
                self.loop_sell(self.price_buy)

    def loop_sell(self, price_buy):
        while True:
            self.price = singl_tool(TOKEN, FIGI[self.figi_name], 'tool_rubl')

            if self.price >= price_buy + self.mpoint(2):
                self.additional_loop(self.price)

                print(self.perfect_price)
                while True:
                    self.price = singl_tool(TOKEN, FIGI[self.figi_name], 'tool_rubl')

                    if self.price >= self.perfect_price + self.mpoint():
                        self.additional_loop(self.price)
                        print(self.perfect_price)
                    if self.price <= self.perfect_price - self.mpoint(1) and self.price >= price_buy + self.mpoint(2):
                        result = sell(TOKEN, FIGI[self.figi_name])
                        print(
                            f"Количество лотов {str(result.lots_requested)}, цена продажи {str(result.initial_order_price.units)}.{str(result.initial_order_price.nano)[:2]}")
                        new_price = float(f'{str(result.initial_order_price.units)}.{str(result.initial_order_price.nano)[:2]}')
                        print(new_price)
                        return new_price
            elif self.price <= price_buy - self.mpoint(1):
                result = sell(TOKEN, FIGI[self.figi_name])
                print(
                    f"Количество лотов {str(result.lots_requested)}, цена продажи {str(result.initial_order_price.units)}.{str(result.initial_order_price.nano)[:2]}")
                new_price = float(f'{str(result.initial_order_price.units)}.{str(result.initial_order_price.nano)[:2]}')
                print(new_price)
                return new_price

    def mpoint(self, coefficient = 1):
        return self.point * coefficient

    def additional_loop(self, price):
        self.perfect_price = price
