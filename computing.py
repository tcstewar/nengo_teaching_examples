import nengo
import numpy as np

model = nengo.Network()
with model:
    a = nengo.Ensemble(n_neurons=100, dimensions=2, radius=1.5)
    stim = nengo.Node([0,0])
    nengo.Connection(stim, a)
    
    b = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    def product(x):
        return x[0]*x[1]
        
    nengo.Connection(a, b, function=product)
