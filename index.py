import dash
import dash_core_components as dcc
import dash_html_components as htmlwrap
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Documentation @https://dash-bootstrap-components.opensource.faculty.ai/

# To link one of the Bootswatch styles, such as Cyborg
app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)

confirmed_case = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
death_case = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

confirmed = pd.read_csv(confirmed_case)
death = pd.read_csv(death_case)
recovered = pd.read_csv(recovered)


app.run_server()