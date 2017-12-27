## Sec5: Exercise 8: Select Widgets - Drawing Spans Dynamically

#Plotting periodic table elements and adding span annotations dynamically
 
#Importing libraries
from bokeh.plotting import figure
from bokeh.io import curdoc, output_file, show
from bokeh.sampledata.periodic_table import elements
from bokeh.models import Range1d, ColumnDataSource
from bokeh.models.annotations import Span
from bokeh.models.widgets import Select
from bokeh.layouts import layout

#Remove rows with NaN values and then map standard states to colors
elements.dropna(inplace=True) #if inplace is not set to True the changes are not written to the dataframe
colormap={'gas':'yellow','liquid':'orange','solid':'red'}
elements['color']=[colormap[x] for x in elements['standard state']]
 
#Create three ColumnDataSources for elements of unique standard states
gas=ColumnDataSource(elements[elements['standard state']=='gas'])
liquid=ColumnDataSource(elements[elements['standard state']=='liquid'])
solid=ColumnDataSource(elements[elements['standard state']=='solid'])
 
#Create the figure object
f=figure()
f.xaxis.axis_label="Atomic radius"
f.yaxis.axis_label="Boiling point"
 
#adding glyphs
f.circle(x="atomic radius", y="boiling point",
         size=gas.data["van der Waals radius"]/10,
         fill_alpha=0.2,color="color",legend='Gas',source=gas)

f.circle(x="atomic radius", y="boiling point",
         size=[i/10 for i in liquid.data["van der Waals radius"]],
         fill_alpha=0.2,color="color",legend='Liquid',source=liquid)

f.circle(x="atomic radius", y="boiling point",
         size=[i/10 for i in solid.data["van der Waals radius"]],
         fill_alpha=0.2,color="color",legend='Solid',source=solid)

# create span lines for min, max, and avg
avg1 = sum(gas.data['boiling point'])/len(gas.data['boiling point'])
max1 = max(gas.data['boiling point'])
min1 = min(gas.data['boiling point'])
gas_line = Span(location=avg1,dimension='width',line_color='yellow',line_width=2)

avg2 = sum(liquid.data['boiling point'])/len(liquid.data['boiling point'])
max2 = max(liquid.data['boiling point'])
min2 = min(liquid.data['boiling point'])
liquid_line = Span(location=avg2,dimension='width',line_color='orange',line_width=2)
 
avg3 = sum(solid.data['boiling point'])/len(solid.data['boiling point'])
max3 = max(solid.data['boiling point'])
min3 = min(solid.data['boiling point'])
solid_line = Span(location=avg3,dimension='width',line_color='red',line_width=2)

f.add_layout(gas_line)
f.add_layout(liquid_line)
f.add_layout(solid_line)

# create function
def update_spans(attr,old,new):
    if select_widget.value == 'avgs':
        gas_line.location=avg1
        liquid_line.location=avg2
        solid_line.location=avg3
    elif select_widget.value == 'maxes': 
        gas_line.location=max1
        liquid_line.location=max2
        solid_line.location=max3
    elif select_widget.value == 'mins':
        gas_line.location=min1
        liquid_line.location=min2
        solid_line.location=min3

# create widgets
options=[('avgs','Avg Boiling Point'),('maxes','Max Boiling Point'),('mins','Min Boiling Point')] # list of tuples of column in CDS and label in dropdown
select_widget = Select(title='Boiling Points - Statistical Value',options=options)
select_widget.on_change('value',update_spans)

lay_out=layout([[select_widget]])

curdoc().add_root(f)
curdoc().add_root(lay_out)