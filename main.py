# Import required modules
import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt


def main():
    # ----- Set starting date and ending date
    start = dt.datetime(2019, 1, 1)
    end = dt.datetime.now()

    # ----- Get finance data
    data = web.DataReader("TSLA", 'yahoo', start, end)

    # Print available styles
    # print(mpf.available_styles())  # ['binance', 'blueskies', 'brasil', 'charles', 'checkers', 'classic', 'default',
    # 'ibd', 'kenan', 'mike', 'nightclouds', 'sas', 'starsandstripes', 'yahoo']

    #
    colors = mpf.make_marketcolors(up="#00ff00", down="#ff0000", wick="inherit",
                                   edge="inherit", volume="in")
    my_style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)
    mpf.plot(data, type="candle", style=my_style)
    # plt.plot(data["Close"])
    # plt.show()


if __name__ == '__main__':
    main()
