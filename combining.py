import nengo
import numpy as np

model = nengo.Network()
with model:
    stim1 = nengo.Node(0)
    stim2 = nengo.Node(0)
    
    a1 = nengo.Ensemble(n_neurons=100, dimensions=1)
    a2 = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    nengo.Connection(stim1, a1)
    nengo.Connection(stim2, a2)
    
    
    
    
    a = nengo.Ensemble(n_neurons=100, dimensions=2, radius=1.5)
    nengo.Connection(a1, a[0])
    nengo.Connection(a2, a[1])

    b = nengo.Ensemble(n_neurons=100, dimensions=1)
    
    def product(x):
        return x[0]*x[1]
        
    nengo.Connection(a, b, function=product)
