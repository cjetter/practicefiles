#########################################################################################################################
# Program visualizes the temp and humidity data via bokeh server
# 
# Data feeds from database generated by SQL_DHTtest_CMJ.py file
# First step is to start a bokeh server by entering "bokeh serve --show 'filename.py'"
#
#########################################################################################################################

#import libraries
import time as t
import datetime as dt 
import pandas as pd
from pandas.tseries.offsets import *
import sqlite3
# from smb.SMBConnection import SMBConnection
from random import randrange
from scipy.signal import savgol_filter
from bokeh.plotting import figure, show
from bokeh.io import curdoc
from bokeh.layouts import column, widgetbox, row
from bokeh.models import *
from bokeh.models.widgets import Button, RadioButtonGroup, RadioGroup, Tabs, Panel, CheckboxGroup
from math import radians

# function to create temperature plot
def make_temp_plot(source):
    #create tools used within temperature figure
    hover = HoverTool(tooltips=[
    ("Fecha", '$x{%m/%d/%Y %H:%M:%S}'),
    ("Temp. (C)", '@y{0.00}')],
    #formatters={'x': 'datetime'},
    mode='vline')
    reset_tool = ResetTool()
    wheel_zoom_tool = WheelZoomTool(dimensions='width')
    pan_tool = PanTool()
    
    # create plot figure
    f_temp = figure(title='Temperatura/Tiempo',x_axis_type='datetime',x_axis_label='tiempo',y_axis_label='temperatura (C)',
    plot_width = 1200,plot_height = 400,tools=[hover,reset_tool,wheel_zoom_tool,pan_tool],y_range=(-5, 25),)#x_range=(start_dt,end_dt))
    f_temp.min_border_bottom=60
    f_temp.title.text_font_size='12pt'
    f_temp.title.text_font_style='bold'
    f_temp.yaxis[0].formatter = NumeralTickFormatter(format='0,0.00')

    #create box annotation to highlight acceptable ranges for temperature
    maxtemp = 40
    mintemp = 20
    low_box = BoxAnnotation(top=mintemp, fill_alpha=0.1, fill_color='light red')
    mid_box = BoxAnnotation(bottom=mintemp, top=maxtemp, fill_alpha=0.1, fill_color='green')
    high_box = BoxAnnotation(bottom=maxtemp, fill_alpha=0.1, fill_color='light red')
    f_temp.add_layout(low_box)
    f_temp.add_layout(mid_box)
    f_temp.add_layout(high_box)

    # Set date format for x_axis of temperature plot
    f_temp.xaxis.formatter=DatetimeTickFormatter(milliseconds=["%m/%d/%Y %H:%M:%S:%3N"],
    seconds=["%m/%d/%Y %H:%M:%S"],
    minsec=["%m/%d/%Y %H:%M:%S"],
    minutes=["%m/%d/%Y %H:%M:%S"],
    hourmin=["%m/%d/%Y %H:%M:%S"],
    hours=["%m/%d/%Y %H:%M:%S"],
    days=["%m/%d/%Y %H:%M:%S"],
    months=["%m/%d/%Y %H:%M:%S"],
    years=["%m/%d/%Y %H:%M:%S"],)
    f_temp.xaxis.major_label_orientation = radians(45)

    #plot line of data
    f_temp.line(source=source,x='x',y='y',line_color='firebrick',line_width=2,legend="temperatura")

# function to create humidity plot
def make_hum_plot(source):
    #create tools used within humidity figure
    hover2 = HoverTool(tooltips=[
        ("Fecha / Hora", '@x{%F}'),
        ("Hum. (%)", '@y{0.00%}')],
        formatters={'x': 'datetime'},
        mode='vline')
    reset_tool2 = ResetTool()
    wheel_zoom_tool2 = WheelZoomTool(dimensions='width')
    pan_tool2 = PanTool()

    #create figure for humedad
    f_hum = figure(title='Humedad/Tiempo',x_axis_type='datetime',x_axis_label='tiempo',y_axis_label='humedad (%)',
    plot_width = 1200,plot_height = 400,tools=[hover2,reset_tool2,wheel_zoom_tool2,pan_tool2],y_range=(0,1),)#x_range=(start_dt,end_dt))
    f_hum.min_border_bottom=60
    f_hum.title.text_font_size='12pt'
    f_hum.title.text_font_style='bold'
    f_hum.yaxis[0].formatter = NumeralTickFormatter(format='0.00%')

    #create box annotation to highlight acceptable ranges for humidity
    maxpercent = .8
    minpercent = .5
    low_box = BoxAnnotation(top=minpercent, fill_alpha=0.1, fill_color='red')
    mid_box = BoxAnnotation(bottom=minpercent, top=maxpercent, fill_alpha=0.1, fill_color='green')
    high_box = BoxAnnotation(bottom=maxpercent, fill_alpha=0.1, fill_color='red')
    f_hum.add_layout(low_box)
    f_hum.add_layout(mid_box)
    f_hum.add_layout(high_box)

    # Set date format for x_axis of humidity plot
    f_hum.xaxis.formatter=DatetimeTickFormatter(milliseconds=["%m/%d/%Y %H:%M:%S:%3N"],
    seconds=["%m/%d/%Y %H:%M:%S"],
    minsec=["%m/%d/%Y %H:%M:%S"],
    minutes=["%m/%d/%Y %H:%M:%S"],
    hourmin=["%m/%d/%Y %H:%M:%S"],
    hours=["%m/%d/%Y %H:%M:%S"],
    days=["%m/%d/%Y %H:%M:%S"],
    months=["%m/%d/%Y %H:%M:%S"],
    years=["%m/%d/%Y %H:%M:%S"],)
    f_hum.xaxis.major_label_orientation = radians(45)

    #plot line of data
    f_hum.line(source=source2,x='x',y='y',line_color='navy',line_width=2,legend="humedad")

#create radio group for setting x-axis range
radio_group_datetime = RadioGroup(labels=["1 Hora","12 Horas", "1 Día", "1 Semana","1 Mes","3 Meses","6 Meses","1 Año","Todo"], active=0)

#create radio button group for specifying whether distribution is discrete or smoothed
radio_button_group_distribution = RadioButtonGroup(labels=["Discrete","Smoothed"], active=0)

# create text label to display x/y coordinates of plots
 

# create toggle for synchronized scrolling


# create toggle for adding box annotation highlight to plot figure


# Function to capture data based on datetime range and distribution type
def get_dataset(src, datetime, distribution):
    df = src.copy()
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    df_columns = list(df.columns)[1:] # return list of data point columns to be smoothed / excludes first column of dates
    if distribution == 'Smoothed':
        window, order = 51, 3
        for key in df_columns:
            df[key] = savgol_filter(df[key], window, order)
    # Apply datetime range to x axis
    # Radio button options are 1Hora, 12 Horas, 1 Día, 1 Semana, 1 Mes, 3 Meses, 6 Meses , 1 Año , Todo
    timenow=pd.Timestamp(dt.datetime.today())
    if datetime == 0: timelimit = timenow - DateOffset(hours=1)
    elif datetime == 1: timelimit = timenow - DateOffset(hours=12)
    elif datetime == 2: timelimit = timenow - DateOffset(days=1)
    elif datetime == 3: timelimit = timenow - DateOffset(weeks=1)
    elif datetime == 4: timelimit = timenow - DateOffset(months=1)
    elif datetime == 5: timelimit = timenow - DateOffset(months=3)
    elif datetime == 6: timelimit = timenow - DateOffset(months=6)
    elif datetime == 7: timelimit = timenow - DateOffset(years=1)
    else: timelimit = 0
    df = df[df['DateTime'] >= timelimit]
    # Need to convert pandas dataframe to dictionary, as periodic callback function has issues with passing in pandas objects??
    x = list(df['DateTime'])
    y_temp = list(df['Temperature'])
    y_hum = list(df['Humidity'])
    source=ColumnDataSource(dict(x=x,y=y_temp))
    source2=ColumnDataSource(dict(x=x,y=y_hum))
    return source, source2

# #from smb.SMBConnection import SMBConnection
#import tempfile
# establish connection to SMB
# userID = 'cmj'
# password = 'dhttest'
# client_machine_name = 'Christophers-Notebook.local' 
# server_name = 'engrack00'
# conn = SMBConnection(userID, password, client_machine_name, server_name, use_ntlm_v2 = True)
# ip = '192.168.1.38'
# portno = 139
# conn.connect(ip, portno)

# file_obj = tempfile.TemporaryFile()
# file_attributes, filesize = conn.retrieveFile('DHT', '/DHT.sqlite', file_obj)

# file_obj.seek(0)
# print(file_obj.read())

# load original datasource


filepath='/Users/Apple/Documents/Programming/Python/Other Projects/Greenhouse/DHT.sqlite'
conn = sqlite3.connect(filepath)
df_original = pd.read_sql('SELECT * FROM LogData',conn)
df_original['DateTime'] = pd.to_datetime(df_original['DateTime'])
df_original.sort_values('DateTime',inplace=True)

distribution='Discrete'
datetime_start = 7

source, source2 = get_dataset(df_original,datetime_start,distribution)
plot_temp = make_temp_plot(source)
plot_hum = make_hum_plot(source2)

# # Treatment of user interaction with widgets
# radio_button_datetime.on_click(my_radio_handler)
# radio_button_group_distribution.on_click(my_radio_handler_distribution)

# def update_plot(new):
#     city = city_select.value
#     src = get_dataset(df, radio_group_datetime.value, radio_button_group_distribution.value)
#     source.data.update(src.data)

# # create periodic function
# def update():
#     conn = sqlite3.connect(filepath0)
#     cur = conn.cursor()
#     cur.execute('''
#                    SELECT * FROM LogData
#                    ORDER BY DateTime DESC LIMIT 1
#                    ''')    
#     x = cur.fetchone()[0]
#     x = list((dt.datetime.strptime(x, '%m/%d/%Y %H:%M:%S'),))
#     cur.execute('''
#                    SELECT * FROM LogData
#                    ORDER BY DateTime DESC LIMIT 1
#                    ''')  
#     y_temp = list((cur.fetchone()[2],))
#     cur.execute('''
#                    SELECT * FROM LogData
#                    ORDER BY DateTime DESC LIMIT 1
#                    ''')  
#     y_hum = list((cur.fetchone()[1],))
#     new_data = dict(x=x,y=y_temp)
#     new_data2 = dict(x=x,y=y_hum)
#     source.stream(new_data)
#     source2.stream(new_data2)


#add figures to curdoc, set layout and configure callback
#controls = column(radio_group_datetime, radio_button_group_distribution)
curdoc().add_root(plot_temp)
#curdoc().add_root(row(f_hum,controls)
curdoc().add_root(radio_group_datetime)
curdoc().add_root(radio_button_group_distribution)
#curdoc().add_periodic_callback(update,6000)