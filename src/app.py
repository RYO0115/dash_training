
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    "background":"#3FFFFF",
    "paper":"#FFFFFF",
    "text":"#7FDBFF"
}

app.layout = html.Div(style={"background": colors["paper"]}, children=[
    html.H1(
        children="Hello Dash",
        style={
            "textAlign":"center",
            "color":colors["text"]
        }
    ),
    html.Div(children="Dash: A web application framework for python", style={
            "textAlign": "left",
            "color":colors["text"]
        }
    ),
    dcc.Graph(
        id="example-graph-z",
        figure={
            "data":[
                {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                {"x": [1,2,3], "y":[4,1,2], "type":"bar", "name":"Montreal"}
            ],
            "layout": {
                "plot_bgcolor": colors["background"],
                "paper_bgcolor": colors["paper"],
                "font": {
                    "color":colors["text"]
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)