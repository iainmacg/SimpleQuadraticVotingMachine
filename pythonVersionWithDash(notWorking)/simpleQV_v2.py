# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:11:54 2020

@author: johnn
"""


import jsdQVIncludes as qv

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

num_sliders = 11
total_budget = 100
oecd_labels = ['Housing','Income','Jobs','Community','Education','Environment','Civic Engagement','Helath','Life Satisfaction','Safety','Work-Life Balance']
        
def addOneSlider(x):
    #print ('adding slider '+str(x))
    return html.Div([
            html.Div([
                html.H3(oecd_labels[x],style={'line-height':'0.1'}),
                html.P(id='output-{}'.format(x),style={'line-height':'0.1'})
            ],style={'float':'left','width':'20%','background-color':'#dddddd','border':'1px solid #999999'}),
            html.Div([
                html.P(),
                dcc.Slider(id='slider-{}'.format(x),
                           step=0.1,
                           value=0,
                           max=total_budget**0.5,
                           marks={0.0: '0', 1: 'whatevs', 5.0: 'face'}
                           )
                ],style={'float':'left','width':'75%','border':'1px solid #999999',})
            ],style={'width':'80%','content':"",'display':'table','clear':'both'})

machine = qv.QuadraticVotingMachine(num_sliders,total_budget)

# to_evaluate = ""
# for i in range(num_sliders):
# to_evaluate += 'addOneSlider('+str(i)+'),\n'

app = dash.Dash() #external_stylesheets=['jsdStyle.css'])
app.layout = html.Div([
    html.H1('Simple quadratic voting macine based with OECD Better Life Index categories'),
    html.H2('Budget remaining: ',id='budget-remaining'),
    addOneSlider(0),
    addOneSlider(1),
    addOneSlider(2),
    addOneSlider(3),
    addOneSlider(4),
    addOneSlider(5),
    addOneSlider(6),
    addOneSlider(7),
    addOneSlider(8),
    addOneSlider(9),
    addOneSlider(10),
    #eval(to_evaluate) # doesn't work and I'm bored trying to fix it and other "list of list" problems
    html.Div(id='intermediate-value', style={'display': 'none'})
    ])


for i in range(num_sliders):
    @app.callback(Output('output-{}'.format(i), 'children'), [Input('slider-{}'.format(i), 'value')])
    def updateOutput(slider_i_value):
        machine.knobMoved(i,slider_i_value)
        #a = "{:0.2f}".format(machine.squared)
        return "%.2f" % machine.squared[10:13]

#for j in range(num_sliders):
@app.callback(Output('budget-remaining', 'children'), [Input('output-0', 'children')])
def updateTheBudget(whatever):
    machine.updateBudget()
    return machine.knobs[0]
### look into this: https://dash.plotly.com/advanced-callbacks

if __name__ == '__main__':
    app.run_server(debug=True)