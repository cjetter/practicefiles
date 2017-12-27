from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc, output_file, show
from math import pi, cos, sin, radians

# establish radius of planets
mars_radius = .7
earth_radius = 1
degree_mars = 0
degree_earth = 0

# create data source
source1 = ColumnDataSource(dict(x1=[mars_radius*cos(radians(degree_mars))],y1=[mars_radius*sin(radians(degree_mars))]))
source2 = ColumnDataSource(dict(x2=[earth_radius*cos(radians(degree_earth))],y2=[earth_radius*sin(radians(degree_earth))]))

# create figure
f=figure(width=500,height=500,x_range=(-2,2),y_range=(-2,2))

# create glyphs
f.circle(x=0,y=0,color='yellow',alpha=.3,size=50)
f.circle(x='x1',y='y1',color='red',size=12,source=source1)
f.arc(x=0,y=0,radius=mars_radius,color='red',start_angle=0,end_angle=2*pi)
f.circle(x='x2',y='y2',color='blue',size=18,source=source2)
f.arc(x=0,y=0,radius=earth_radius,color='blue',start_angle=0,end_angle=2*pi)

# create callback function
def update():
    global degree_mars, degree_earth
    degree_mars = degree_mars+1
    degree_earth = degree_earth+2
    a1 = mars_radius*cos(radians(degree_mars))
    b1 = mars_radius*sin(radians(degree_mars))
    new_data1 = dict(x1=[a1],y1=[b1])
    source1.stream(new_data1,rollover=1)
    a2 = earth_radius*cos(radians(degree_earth))
    b2 = earth_radius*sin(radians(degree_earth))
    new_data2 = dict(x2=[a2],y2=[b2])
    source2.stream(new_data2,rollover=1)

# add figure and callback to current document
curdoc().add_root(f)
curdoc().add_periodic_callback(update,50)