# %%
import numpy as np

def createLayer(prevLayerSize, layerSize):
    weights = np.random.rand(prevLayerSize,layerSize)
    biases = np.random.rand(prevLayerSize)
    values = np.ones(layerSize)
    return [weights, biases, values]


def updateLayer(prevLayer, layer):
    layer[2] = prevLayer[2]*layer[0]+layer[1]

def createNetwork(layersSizes):
    layers = [createLayer(i,i+1) for i in range(len(layersSizes)-1)]
    return layers

def updateNetwork(inputs, network):
    network[0][2] = inputs
    for i in range(len(network)-1):
        updateLayer(network[i],network[i+1])

# %%
net = createNetwork([2,2,2])
for layer in range(len(net)):
    print(net[layer])
    print("\n")
# %%
updateNetwork([1,2], net)