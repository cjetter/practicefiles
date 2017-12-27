# flask app

from flask import Flask, render_template
from datetime import datetime
from BasicLine import script, html, cdn_js, cdn_css

# initiate the flask app
app_delete = Flask(__name__)

# create the index page function
@app_delete.route("/")
def index():
    return render_template('index.html',js=script,div=html,cdn_js=cdn_js,cdn_css=cdn_css)

# run the app
if __name__ == '__main__':
    app_delete.run(debug=True)  ## when deploying app online, its good to mark to false (prevent visitors to the webpage from seeing python errors)