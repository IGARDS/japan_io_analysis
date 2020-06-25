from gurobipy import *

model = read('jpn1995.lp')

model.setParam( 'Method', -1 )

model.optimize()