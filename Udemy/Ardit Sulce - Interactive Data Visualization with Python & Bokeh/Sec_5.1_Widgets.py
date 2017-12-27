## Widgets in static bokeh

## NOTE: 
## This program will not generate the output without use of bokeh server.
## The code is run and then interrupted, not remaining active to interact with the html file.
## Essentialy it is a useless piece of code, as it is not interactive on its own.

# import libraries
from bokeh.io import output_file, show
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

# prepare bokeh output file
output_file('simple_bokeh.html')

# prepare widgets
text_input = TextInput(value='Ardit')
button=Button(label='Generate Text')
output=Paragraph()

def update():
    output.text = 'Hello, '+text_input.value

button.on_click(update)

lay_out = layout([[text_input,button],[output]])

show(lay_out)