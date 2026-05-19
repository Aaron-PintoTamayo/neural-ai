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

lr = 0.1 #learning rate

for epoch in range(100000):
    total_error=0
    for i in range(len(inputs)):
        x=inputs[i]
        t=targets[i]
        z=(x[0]*weight1)+(x[1]*weight2)+bias
        output=sigmaoid(z)

        error=t-output
        total_error = total_error + error ** 2 #squared to remove negative

        delta = error * sigmaoid_derivative(z)

        weight1+=x[0]*lr*delta
        weight2+=x[1]*lr*delta
        bias+=lr*delta
    if epoch % 100 == 0:
        print(f"epoch {epoch} error {round(total_error, 6)}")

print("\nresults:")
for i in range(len(inputs)):
    x = inputs[i]
    z = (x[0] * weight1) + (x[1] * weight2) + bias
    output = sigmaoid(z)
    print(f"input {x} target {targets[i]} output {round(output, 3)} answer {round(output)}")    
