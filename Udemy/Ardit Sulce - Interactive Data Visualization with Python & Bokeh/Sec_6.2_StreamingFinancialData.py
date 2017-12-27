from random import randrange
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import requests
from bs4 import BeautifulSoup

# create webscraping function to extract value
def scrape():
    r = requests.get('http://bitcoincharts.com/markets/btcnCNY.html',headers={'User-Agent':'Mozilla/5.0'})
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    value_raw = list(soup.find_all("p"))
    value_net = float(value_raw[0].span.text)
    return value_net

# create the data source
source = ColumnDataSource(dict(x=[1],y=[scrape()]))

# create the figure
f=figure()

# create the glyphs
f.circle(x='x',y='y',source=source,color='olive',line_color='firebrick')
f.line(x='x',y='y',source=source,line_color='seagreen')

# define callback function
def update():
    new_data=dict(x=[source.data['x'][-1]+1],y=[scrape()])
    source.stream(new_data,rollover=200)  # rollover defines how many data points you maintain in the plot removing by LIFO
    print(source.data)

# add figure to bokeh application
curdoc().add_root(f)
curdoc().add_periodic_callback(update,2000)  ## execute specific function every 10 seconds


