import sys

def ticker_symbols(ticker):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    rev_com = dict(zip(COMPANIES.values(), COMPANIES.keys()))
    if ticker in STOCKS:
        print(rev_com[ticker], STOCKS[ticker], sep=' ')
    else:
        print('Unknown ticker')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        ticker_symbols(sys.argv[1].upper())

