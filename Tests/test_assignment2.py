"""Test for the assignment_2.py program."""

import numpy
import unittest
from matplotlib import pyplot as plt
from Python_SciPy.Assignment_2.assignment_2 import VoltageData

class TestCore(unittest.TestCase):
    """Test methods class."""

    def tests(self):
        # Load some data
        t, v = numpy.loadtxt('Python_SciPy/Assignment_2/sample_data_file.txt', unpack=True)
        v_data = VoltageData(t, v)
        # Test len()
        assert len(v_data) == len(t)
        # Test the timestamps attribute
        assert numpy.all(v_data.voltages == v)
        # Test the voltages attribute
        assert numpy.all(v_data.timestamps == t)
        # Test square parenthesis
        assert v_data[3, 1] == v[3]
        assert v_data[-1, 0] == t[-1]
        # Test slicing
        assert numpy.all(v_data[1:5, 1] == v[1:5])
        # Test iteration
        for i, entry in enumerate(v_data):
            assert entry[0] == t[i]
            assert entry[1] == v[i]
        # Test printing
        print(v_data)
        # Test plotting
        v_data.plot(fmt='ko', markersize=5, label='normal voltage')
        x_grid = numpy.linspace(min(t), max(t), 200)
        plt.plot(x_grid, v_data(x_grid), 'r-', label='spline')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    unittest.main()
