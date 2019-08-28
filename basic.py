import nengo
import numpy as np

model = nengo.Network()
with model:
    
    a = nengo.Ensemble(n_neurons=3, dimensions=1,
                       neuron_type=nengo.LIF(tau_rc=0.02, tau_ref=0.002),
                       bias=np.zeros(3),
                       gain=np.ones(3))
    
    stim = nengo.Node([0,0,0])
    nengo.Connection(stim, a.neurons)