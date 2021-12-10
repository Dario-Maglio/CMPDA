"""Modelling agent behaviours in a competitive framework"""

import numpy as np
import matplotlib.pyplot as plt

from keras.models import Model
from keras.layers import Input, Dense
from tensorflow.keras.utils import plot_model

N = 10
MAX_M = 4
MAX_S = 4

np.random.seed(42)

names = ['Agent '+str(i+1) for i in range(N)]
memories = np.random.randint(1, MAX_M, size=N)
strategies =  np.random.randint(1, MAX_S, size=N)
history = [1. for i in range(MAX_M + 1)]

class Agent:
    """Neural network describing the agent behaviour with a memory of M last
       results and S possible strategies to apply.
    """
    def __init__(self, name, M, S):
        """Take the agent name, memory and number of strategies, then compile
           its NN and ?
        """
        self._name = str(name)
        self._M = M
        self._S = S

        inputs = Input(shape=(self._M,))
        strategies = Dense(self._S, activation='sigmoid')(inputs)
        outputs = Dense(1, activation='sigmoid')(strategies)
        self._model = Model(inputs=inputs, outputs=outputs, name=self._name)
        self._model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    @property
    def name(self):
        return self._name

    @property
    def memory(self):
        return self._M

    @property
    def strategies(self):
        return self._S

    def strategies_summary(self):
        self._model.summary()
        plot_model(self._model)

    def __call__(self, Tseq):
        """Evaluates the behaviour of the agent after a given time sequence.
        """
        return self._model.predict(Tseq[0:self._M])

agents = Agent(names[0], memories[0], strategies[0])
print(agents.name)
print(agents.memory)
print(agents.strategies)
print(agents.strategies_summary())
print(agents(history))
