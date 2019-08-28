import nengo
import numpy as np

model = nengo.Network()
with model:
    
    a = nengo.Ensemble(n_neurons=10, dimensions=1,
                       neuron_type=nengo.LIF(tau_rc=0.02, tau_ref=0.002),
                       bias=np.zeros(10),
                       gain=np.ones(10))
    
    stim = nengo.Node(0)
    nengo.Connection(stim, a.neurons[0])
    
    w = np.zeros((10,10))
    for i in range(9):
        w[i+1, i] = 0.1
    nengo.Connection(a.neurons, a.neurons, transform=w, synapse=0.001)