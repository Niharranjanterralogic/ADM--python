# from bokeh.plotting import figure
# from bokeh.io import output_file,show
# x=[3,7.4,10]
# y=[3,6,9]
# output_file("hk.html")
# f=figure()
# f.circle(x,y)
# show(f)

#######################################Plotting Educations Data ##########################


# from bokeh.plotting import figure
# from bokeh.io import output_file,show
# import pandas
# df=pandas.read_csv("https://pythonizing.github.io/data/bachelors.csv")
# x=df["Year"]
# y=df["Engineering"]

# output_file("line_from_bachelors.html")
# f=figure()
# f.line(x,y)
# show(f)

#################  changing plot properties #####################
# import pandas
# from bokeh.plotting import figure, output_file, show
 
# p=figure(plot_width=500,plot_height=400, tools='pan',logo=None)
 
# p.title.text="Cool Data"
# p.title.text_color="Gray"
# p.title.text_font="times"
# p.title.text_font_style="bold"
# p.xaxis.minor_tick_line_color=None
# p.yaxis.minor_tick_line_color=None
# p.xaxis.axis_label="Date"
# p.yaxis.axis_label="Intensity"    
 
# p.line([1,2,3],[4,5,6])
# output_file("graph.html")
# show(p)



#################### PLOTING WEATHER DATA ####################

import pandas
from bokeh.plotting import figure,output_file,show
df=pandas.read_excel("verlegenhuken.xlsx",sheet_name=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10
 
p=figure(plot_width=500,plot_height=400,tools='pan')

p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"    
 
p.circle(df["Temperature"],df["Pressure"],size=0.5)
output_file("Weather.html")
show(p)