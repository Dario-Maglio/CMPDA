"""Excercising with classes and Hopfield neural networks."""

import numpy as np
#from matplotlib import pyplot as plt

class NeuralCluster:
    """General neural cluster. Name and number of neurons as inputs."""
    def __init__(self, cluster_name, num_neur):
        self._clustername = cluster_name
        self._numneur = num_neur
        print(f'{cluster_name} created.')
        self._states = -np.ones(num_neur)
        self._weights = np.zeros((num_neur, num_neur))
        self._threshold = np.zeros(num_neur)

    def __str__(self):
        return self._clustername

    def __getitem__(self, index):
        return self._states[index]

    def __setitem__(self, index, new_value):
        self._states[index] = new_value

    def __len__(self):
        return len(self._states)

    def __iter__(self):
        return iter(self._states)

    def __call__(self, inp):
        for data in inp:
            self.output(data)

    @property
    def num_neur(self):
        """Number of neuron of the neural network"""
        return self._numneur

    @num_neur.setter
    def num_neur(self, new_value):
        print(f'Unable to change the number of neurons.')

    def training(self, patterns):
        """First supervisioned training of the cluster."""

    def update_weights(self):
        """Weights and threshold upgrade at the end of the update."""

    def update_states(self):
        """Update of the neural states."""

    def output(self, inp):
        """Give an output attractor pattern for each input pattern."""
        self._states = inp

VIEW = NeuralCluster("Visual cluster", 25)
VIEW.num_neur = 5
print(VIEW[4])
print(VIEW)
