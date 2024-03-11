from SETTING import TOKEN
from figi import add_figi
from tinkoff.invest import Client
from tinkoff.invest.services import InstrumentsService






def figi_by_ticker(ticker: str):
    """Example - How to get figi by name of ticker."""

    with Client(TOKEN) as client:
        instruments: InstrumentsService = client.instruments
        tickers = []
        figi = ''
        for method in ["shares", "bonds", "etfs", "currencies", "futures"]:
            for item in getattr(instruments, method)().instruments:
                tickers.append(
                    {
                        "ticker": item.ticker,
                        "figi": item.figi,
                    }
                )
        for data in tickers:
            if data['ticker'] == ticker:
                figi = data['figi']
        if not figi:
            print('не то')
            return


        print(f"\nTicker {ticker} have figi={figi}\n")
        add_figi(ticker, figi)


if __name__ == "__main__":
    main('CHMF')
