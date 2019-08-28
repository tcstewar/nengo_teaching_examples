import nengo
import numpy as np
model = nengo.Network()
with model:
    stim_food = nengo.Node([0,0])
    food = nengo.Ensemble(n_neurons=200, dimensions=2)
    food.radius = 1.4
    nengo.Connection(stim_food, food)
    
    stim_light = nengo.Node(0)
    light = nengo.Ensemble(n_neurons=100, dimensions=1)
    nengo.Connection(stim_light, light)
    
    motor = nengo.Ensemble(n_neurons=200, dimensions=2,
                           radius=1.4)
    
    do_food = nengo.Ensemble(n_neurons=300, dimensions=3,
                             radius=1.5)
    nengo.Connection(food, do_food[:2])
    nengo.Connection(light, do_food[2])
    
    position = nengo.Ensemble(n_neurons=2000, dimensions=2,
                              radius=1)
    nengo.Connection(position, position, synapse=0.1)
    nengo.Connection(motor, position, 
                     transform=0.1, synapse=0.1)
    
    def food_func(x):
        food_x, food_y, light = x
        if light > 0:
            return 0, 0
        else:
            return food_x, food_y
    nengo.Connection(do_food, motor, function=food_func)
    
    do_home = nengo.Ensemble(n_neurons=300, dimensions=3,
                             radius=1.5)
    nengo.Connection(position, do_home[:2])
    nengo.Connection(light, do_home[2])
    
    def home_func(x):
        pos_x, pos_y, light = x
        
        if light > 0:
            return -pos_x, -pos_y
        else:
            return 0, 0
    nengo.Connection(do_home, motor, function=home_func)    
    
