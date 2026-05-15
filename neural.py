import math
import random
random.seed(93)
def rand():
    return random.uniform(-1, 1)
weight1=rand()
weight2=rand()
bias=rand()

def sigmaoid(z):
    output=1/(1+math.pow(math.e,-z)) # this uses negative z since a high z which 
                                     # means yes would turn into a small number which is opposite
    return output

def sigmaoid_derivative(z):
    rate=(1-sigmaoid(z))*(sigmaoid(z))# tells us how much a change in z would effect output at any given point
                                      # say z is at 4 if we chagne it slighly there
                                      # then output would change a lot even by slight change but at different points 
                                      # output changes less based on z 
    return rate
inputs  = [[0,0], [0,1], [1,0], [1,1]]
targets = [0, 0, 0, 1]

lr = 0.1

