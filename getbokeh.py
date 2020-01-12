
from bokeh.plotting import figure
from bokeh.io import show, output_notebook
from bokeh.embed import components
import pandas as pd
import quandl


import numpy as np


def get_df_from_ticker(ticker) -> pd.DataFrame:
    quandl.ApiConfig.api_key = "oidGzZN8eMyV6V6thRoT"
    return quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, ticker = [ticker], date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })

def bokeh(ticker):
    data = get_df_from_ticker(ticker)
    p = figure(plot_height=600, plot_width=700,
               title="Quandl WIKI Stock price", x_axis_type='datetime')

    x = np.arange(0,10,0.1)
    y = np.sin(x)
    r = p.line(data.date, data.close, line_width=1)
 #   r = p.line(x,y, line_width=1)
   # show(p, notebook_handle=True)

    print("end of bokeh() fcn")
    return components(p)
