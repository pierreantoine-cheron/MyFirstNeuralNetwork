# %%
import numpy as np

inputs = [1, 2, 3, 4, 5]

weights = [
    [0.1, 0.2, 0.5, 0.4, 0.9],
    [0.5, 0.3, 0.2, 0.2, 0.1],
    [0.3, 0.7, 0.2, 0.7, 0.6]
]

biases = [4, -2.3, 2]


output = []

for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    output.append(neuron_output)
print(output)
# %%
