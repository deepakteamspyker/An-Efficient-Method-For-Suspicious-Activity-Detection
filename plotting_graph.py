from MotionDetector import df #import the daraframe from the MotionDetector
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S") #convert time to a string format
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")


cds=ColumnDataSource(df)

#the dataframe of time values is plotted on the browser using bokeh plots
p=figure(x_axis_type='datetime',height=100, width=500, title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid.ticker= [2,3.5,4]

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q=p.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

output_file("Graph1.html")
show(p)
