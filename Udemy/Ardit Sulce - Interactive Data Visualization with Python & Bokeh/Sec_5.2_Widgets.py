## Sec 5.2 : Widgets in Interactive Bokeh Server Apps
## launch with 'python3 -m bokeh serve app.py' or
## launch with 'bokeh serve app.py' or 'bokeh serve --show app.py'

# import libraries
from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

# prepare widgets
text_input = TextInput(value='Ardit')
button=Button(label='Generate Text')
output=Paragraph()

def update():
    output.text = 'Hello, '+text_input.value

button.on_click(update)

lay_out = layout([[text_input,button],[output]])

curdoc().add_root(lay_out)