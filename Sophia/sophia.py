"""Excercising with classes and Hopfield neural networks."""

import numpy as np

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
        self.output(inp)

    @property
    def num_neur(self):
        """Number of neuron of the neural network"""
        return self._numneur

    @num_neur.setter
    def num_neur(self, new_value):
        print(f'Unable to change the number of neurons externally.')

    def training(self, patterns):
        """First supervisioned training of the cluster."""

    def update_weights(self):
        """Weights and threshold upgrade at the end of the update."""

    def update_states(self):
        """Updates of the states until a dynamical attractor is reached."""

    def output(self, inp):
        """Gives an output attractor pattern for each input pattern."""
        self._states = inp
        self.update_states()
        return self._states

    def energy(self):
        """Calculates the total energy of the neural state."""
        return sum(self._states)

class VisualCluster(NeuralCluster):
    """A neural cluster for picture inputs."""
    def __init__(self, num_neur):
        """Derived class for visual stimuli."""
        NeuralCluster.__init__(self, "Visual cluster", num_neur)


#------------------------------------------------------------------------------
"""Verifying operations on clusters."""

VIEW = NeuralCluster("Taste cluster", 25)
print(VIEW)
VIEW.num_neur = 5
print(VIEW.energy())
for i, stat in enumerate(VIEW):
    if stat == -1:
        stat = 1
    VIEW[i] = stat
print(VIEW[4])

VIEW2 = VisualCluster(16)
print(VIEW2)
VIEW2.num_neur = 5
print(VIEW2.energy())
for i, stats in enumerate(zip(VIEW, VIEW2)):
    VIEW2[i] = (stats[1] + stats[0])/2
print(VIEW2[4])
