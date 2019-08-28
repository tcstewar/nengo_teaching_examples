import nengo
import numpy as np


model = nengo.Network()
with model:
    
    N = 4
    stim = nengo.Node([0]*N)
    
    wta = nengo.networks.EnsembleArray(n_neurons=50, n_ensembles=N)
    
    nengo.Connection(stim, wta.input)
    
    def relu(x):
        return x[0] if x[0]>0 else 0
    wta.add_output('relu', function=relu)
    
    w = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if i == j:
                w[i][j] = 0.5
            else:
                w[i][j] = -0.5
                
    nengo.Connection(wta.relu, wta.input, transform=w)
    
    
    