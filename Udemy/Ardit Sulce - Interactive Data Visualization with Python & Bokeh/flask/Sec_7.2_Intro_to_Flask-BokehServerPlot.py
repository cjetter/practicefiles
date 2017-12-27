# flask app
# must first grant access for the flask app from the bokeh server by passing the following within the command line: 'bokeh serve --allow-websocket-origin=localhost:5000 RandomGenerator.py'

from flask import Flask, render_template
from bokeh.embed import autoload_server

# initiate the flask app
app = Flask(__name__)

# create the index page function
@app.route("/")
def index():
    url = 'http://localhost:5006/RandomGenerator'
    bokeh_script = autoload_server(url=url)
    return render_template('index_plot2.html',bokeh_script=bokeh_script)

# run the app
if __name__ == '__main__':
    app.run(debug=True)  ## when deploying app online, its good to mark to false (prevent visitors to the webpage from seeing python errors)