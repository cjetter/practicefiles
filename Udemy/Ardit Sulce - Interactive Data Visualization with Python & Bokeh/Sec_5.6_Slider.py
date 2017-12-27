## Sec 5.6 - Slider Widgets: Filtering Glyphs, Part 1

#importing libraries
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select, Slider, RadioGroup
from bokeh.layouts import layout, row, column
import pandas as pd 

#crate columndatasource
source_original=ColumnDataSource(dict(average_grades=[7,8,9],
                             exam_grades=[6,9,8],
                             student_names=["Stephan","Helder","Riazudidn"]))

source=ColumnDataSource(dict(average_grades=[7,8,9],
                             exam_grades=[6,9,8],
                             student_names=["Stephan","Helder","Riazudidn"]))

#create the figure
f = figure(x_range=(0,11),
           y_range=(0,11))

#add labels for glyphs
labels=LabelSet(x="average_grades",y="exam_grades",text="student_names",x_offset=5, y_offset=5, source=source)
f.add_layout(labels)

#create glyphs
f.circle(x="average_grades", y="exam_grades", source=source, size=8)

# create function
def update_labels(attr,old,new):
    labels.text=select_widget.value

def update_slider(attr,old,new):
    if radio_group.active == 0: grade_type=str(options2[0])
    elif radio_group.active == 1: grade_type=str(options2[1])
    source.data={key:[value for i, value in enumerate(source_original.data[key]) if source_original.data[grade_type][i]>=slider_widget.value] for key in source_original.data}
   
# create widgets
options=[('student_names','Student Names'),('average_grades','Average Grades'),('exam_grades','Exam Grades')] # list of tuples of column in CDS and label in dropdown
select_widget = Select(title='Attribute',options=options)
select_widget.on_change('value',update_labels)

slider_widget = Slider(start=f.x_range.start,end=f.x_range.end,step=1,value=f.x_range.start)
slider_widget.on_change('value',update_slider)

options2=['average_grades','exam_grades'] # list of strings of column in CDS
radio_group = RadioGroup(labels=options2,active=0)
radio_group.on_change('active',update_slider)

col1=column(select_widget,radio_group,slider_widget)

row1 = row(f,col1)

curdoc().add_root(row1)