from main import df
from bokeh.plotting import figure, show, output_file

p=figure(x_axis_type="datetime",responsive=True,title="Motion Detector Graph")

p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

p=p.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="Green")

output_file("Graph.html")
show(p)
