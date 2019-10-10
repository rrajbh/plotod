#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Thu Sep 12 17:39:27 2019

#@author: rajat.rajbhandari
#"""
#source: https://plot.ly/python/lines-on-maps/


import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go

path1='/Users/rajat.rajbhandari/Documents/GitHub/plotod/traffic1.csv'
df_airports = pd.read_csv(path1)
df_airports.head()
#print(df.columns)

#consigneeLat	,   consigneeLong, consigneeCity	,consigneeState,	consigneeZipCode	, 
#createdAt,	createdAtDateOnly,tripDistance, pricePerMile, 	openingRate	, equipmentType,
#shipperLat, shipperLong	shipperCity	shipperState	shipperZipCode

path2='/Users/rajat.rajbhandari/Documents/GitHub/plotod/flightpath1.csv'
df_flight_paths = pd.read_csv(path2)
df_flight_paths.head()

df_flight_paths['text'] = df_flight_paths['airline'] + ', ' + df_flight_paths['airport1'] + ', ' + df_flight_paths['airport2'] 

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = df_airports['lon'],
    lat = df_airports['lat'],
    hoverinfo = 'text',
    text = df_airports['airport'],
    mode = 'markers',
    marker = dict(
        size = 2,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))

flight_paths = []
for i in range(len(df_flight_paths)):
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i]],
            lat = [df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i]],
            mode = 'lines',
            line = dict(width = 1,color = 'red'),
            text = df_flight_paths['text'],
            opacity = float(df_flight_paths['cnt'][i]) / float(df_flight_paths['cnt'].max()),
        )
    )

fig.update_layout(
    title_text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
    showlegend = False,
    geo = go.layout.Geo(
        scope = 'north america',
        #scope = 'usa',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
)

#fig.show()
plot(fig) #to plot in a default browser.

