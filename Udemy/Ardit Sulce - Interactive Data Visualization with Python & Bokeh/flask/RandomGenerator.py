# random generator plot

from bokeh.models import ColumnDataSource
from bokeh.io import curdoc
from bokeh.plotting import figure
from random import randrange

# create the data source
source = ColumnDataSource(dict(x=[],y=[]))

# create the figure
f=figure(x_range=(0,10),y_range=(0,10))
f.circle(x='x',y='y',color='steelblue',size=10,alpha=.8,source=source)
f.line(x='x',y='y',color='steelblue',alpha=.5,source=source)

# create callback function
def update_plot():
    new_data = dict(x=[randrange(1,10)],y=[randrange(1,10)])
    source.stream(new_data,rollover=15)

# add figure to current document
curdoc().add_root(f)
curdoc().add_periodic_callback(update_plot,1000)