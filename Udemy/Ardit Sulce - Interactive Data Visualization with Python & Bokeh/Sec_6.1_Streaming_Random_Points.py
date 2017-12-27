from random import randrange
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# create the data source
source = ColumnDataSource(dict(x=[],y=[]))

# create the figure
f=figure(x_range=(0,11),y_range=(0,11))

# create the glyphs
f.circle(x='x',y='y',source=source,color='olive',line_color='firebrick')
f.line(x='x',y='y',source=source,line_color='seagreen')

# define callback function
def update():
    new_data=dict(x=[randrange(1,10)],y=[randrange(1,10)])
    source.stream(new_data,rollover=15)  # rollover defines how many data points you maintain in the plot removing by LIFO
    print(source.data)

# add figure to bokeh application
curdoc().add_root(f)
curdoc().add_periodic_callback(update,1000)  ## execute specific function every 1000 miliseconds


