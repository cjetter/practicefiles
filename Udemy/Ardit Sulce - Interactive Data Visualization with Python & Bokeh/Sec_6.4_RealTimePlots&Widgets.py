from random import randrange
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, NumeralTickFormatter
from bokeh.models.widgets import Select
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
from math import radians
from pytz import timezone

# create the data source
source = ColumnDataSource(dict(x=[],y=[]))

# create the figure
f=figure(x_axis_type='datetime')

#customize the x axis datetime formatting
f.xaxis.formatter=DatetimeTickFormatter(
    milliseconds=["%m/%d/%Y %H:%M:%S:%3N"],
    seconds=["%m/%d/%Y %H:%M:%S"],
    minsec=["%m/%d/%Y %H:%M:%S"],
    minutes=["%m/%d/%Y %H:%M:%S"],
    hourmin=["%m/%d/%Y %H:%M:%S"],
    hours=["%m/%d/%Y %H:%M"],
    days=["%m/%d/%Y"],
    months=["%b-%Y"],
    years=["%Y"],)
f.xaxis.major_label_orientation=radians(45)
f.yaxis.formatter=NumeralTickFormatter(format='$ 0,0.00')

# create the glyphs
f.circle(x='x',y='y',source=source,color='olive',line_color='firebrick')
f.line(x='x',y='y',source=source,line_color='seagreen')

# create callback function for widget
def update_url(attr,old,new):
    source.data = dict(x=[],y=[])
    update()

# create widget
CHBTC_url = 'https://bitcoincharts.com/markets/chbtcCNY.html'
BTCChina_url = 'https://bitcoincharts.com/markets/btcnCNY.html'
OKCoin_url = 'https://bitcoincharts.com/markets/okcoinCNY.html'
options = [(BTCChina_url,'BTC China (CNY)'),(CHBTC_url,'CHBTC (CNY)'),(OKCoin_url,'OKCoin (CNY)')]
bitcoin_select = Select(title='Bitcoin Markets - China',options=options,value=options[0][0])  
bitcoin_select.on_change('value',update_url)

# create webscraping function to extract value
def scrape(url=bitcoin_select.value):
    r = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    value_raw = list(soup.find_all("p"))
    value_net = float(value_raw[0].span.text)
    return value_net

# define callback function for datastream
def update():
    new_data=dict(x=[dt.now()],y=[scrape(bitcoin_select.value)])
    source.stream(new_data,rollover=200)  # rollover defines how many data points you maintain in the plot removing by LIFO
    #print(source.data)

# add figure to bokeh application
curdoc().add_root(f)
curdoc().add_root(bitcoin_select)
curdoc().add_periodic_callback(update,2000)  ## execute specific function every 10 seconds