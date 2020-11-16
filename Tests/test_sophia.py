import unittest
from Machine_learning.Sophia.sophia import NeuralCluster, VisualCluster

class TestCore(unittest.TestCase):
    """Test methods class."""

    def test_1(self):
        """Verifying instance functionalities."""
        VIEW = NeuralCluster("Taste cluster", 25)
        assert str(VIEW) == "Taste cluster"
        VIEW.num_neur = 5
        assert VIEW.num_neur == 25
        for i, stat in enumerate(VIEW):
            VIEW[i] = -stat

        VIEW2 = VisualCluster(16)
        print(VIEW2)
        VIEW2.num_neur = 5
        print(VIEW2.energy())
        for i, stats in enumerate(zip(VIEW, VIEW2)):
            print((stats[1] + stats[0])/2)
        self.assertAlmostEqual(VIEW2.energy()/VIEW2.num_neur + VIEW.energy()/VIEW.num_neur, 0.)

if __name__ == "__main__":
    unittest.main()
