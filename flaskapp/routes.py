from flaskapp import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

@app.route("/")
def index():
    #Graph one
    df = px.data.medals_wide()
    fig1 = px.bar(df, x="nation", y=['gold', 'silver', 'bronze', title = 'widespread'])
    return render_template("index.html")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", title = "Home", graph1JSON=graph1JSON)


if __name__ == "__main__":
    app.run(debug=True)