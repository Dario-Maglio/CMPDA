"""Second assignment."""

import numpy
from matplotlib import pyplot as plt
from scipy import interpolate

class VoltageData:
    """Class for handling a set of measurements of the voltage at different
    times."""
    def __init__(self, times, voltages):
        self._data = numpy.column_stack([numpy.array(times, dtype=numpy.float64),
                                         numpy.array(voltages, dtype=numpy.float64)])
        self.spline = interpolate.InterpolatedUnivariateSpline(self.timestamps, self.voltages, k=3)

    @property
    def timestamps(self):
        """Return times."""
        return self._data[:, 0]

    @property
    def voltages(self):
        """Return voltages."""
        return self._data[:, 1]

    def __len__(self):
        """Return the number of measurements (raw number of the matrix)."""
        return len(self._data)

    def __getitem__(self, index):
        """Random access. It gives access with square brackets."""
        return self._data[index]

    def __iter__(self):
        """Inherits iterability"""
        return iter(self._data)

    def __str__(self):
        data_string = []
        for i, entry in enumerate(self):
            data_string.append(f'{i+1}.) {entry[0]} --> {entry[1]}')
        return '\n'.join(data_string)

    def plot(self, axes=None, fmt='bo--', **kwargs):
        """ Plot the data using matplotlib.pyplot."""
        if axes is not None:
            plt.sca(axes)
        else:
            plt.figure('Voltages vs times')
        plt.plot(self.timestamps, self.voltages, fmt, **kwargs)
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.grid(True)
        return plt.gca()

    def __call__(self, value):
        """ Return the voltage value interpolated at time t"""
        return self.spline(value)


if __name__ == '__main__':
    """ Here we test the functionalities of our class. These are not proper
    UnitTest - which you will se in a future lesson."""
    # Load some data
    t, v = numpy.loadtxt('sample_data_file.txt', unpack=True)
    # Test the constructor
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
    #plt.gca returns a value for axis
    x_grid = numpy.linspace(min(t), max(t), 200)
    plt.plot(x_grid, v_data(x_grid), 'r-', label='spline')
    plt.legend()
    plt.show()
