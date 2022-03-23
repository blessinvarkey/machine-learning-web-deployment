from flask import Flask, redirect, url_for, render_template
#import pandas as pd
#import plotly.graph_objs as go
#import plotly, json
app = Flask(__name__)

#graph_one = [go.Scatter(
#    x = data[0],[1],
#   y = data[0],[2],
#    mode = 'lines',
#   name = country
#)]
#layout_one = dict(title = "Gender Distribution", 
#       xaxis = dict(title = '',
#        autotick=False, tick0='Male'

#        ))

@app.route("/")
def home():
    return render_template('index.html')



if __name__=="__main__":
    app.run()