## making a basic line bokeh graph

# importing bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.embed import components
from bokeh.resources import CDN

# prepare some datasets
x = [1,2,3,4,5]
y = [1,2,3,4,5]

# create the figure
f = figure()

# create the glyph line plot
f.line(x,y)

script, html = components(f)

cdn_js = CDN.js_files[0]
cdn_css = CDN.css_files[0]