from bokeh.plotting import figure, curdoc 
from bokeh.io import output_notebook, show
from bokeh.layouts import column
from bokeh.models import Slider, ColumnDataSource, CheckboxGroup
import numpy as np
from numpy import cos, linspace

p = figure(height = 300)
chbox_ruido = CheckboxGroup(
	labels=['Ruido'], active=[])        
slider = Slider(start=0, end=10, value=1, step=0.1, title="batata")

curdoc().add_root(column(slider, chbox_ruido, p))

x = linspace(-6, 6, 200)
y = cos(x)
ruido = np.zeros(y.shape)
if chbox_ruido.active:
	ruido = 0.2*np.random.randn(y.size)
	
source = ColumnDataSource({'x': x, 'y': y + ruido})
p.line('x', 'y', source=source)

def slider_change(attr, old, new):
	
	if chbox_ruido.active:
		ruido = 0.2*np.random.randn(y.size)
	else:
		ruido = np.zeros(y.shape)
		
	source.data = {'x': x, 'y': cos(new*x) + ruido}

def chbox_ruido_change(attr, old, new):
	
	if new:
		ruido = 0.2*np.random.randn(y.size)
	else:
		ruido = np.zeros(y.shape)
		
	source.data = {'x': x, 'y': cos(slider.value*x) + ruido}
	
slider.on_change('value', slider_change)
chbox_ruido.on_change('active', chbox_ruido_change)