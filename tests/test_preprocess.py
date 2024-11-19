import unittest
import numpy as np
from src.preprocess import normalize_point_cloud, voxel_grid_downsample, filter_noise

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        self.sample_points = np.random.rand(1000, 3)

    def test_normalize(self):
        normalized_points = normalize_point_cloud(self.sample_points)
        self.assertAlmostEqual(np.mean(normalized_points), 0, delta=1e-6)

    def test_voxel_downsample(self):
        downsampled_points = voxel_grid_downsample(self.sample_points, voxel_size=0.1)
        self.assertTrue(len(downsampled_points) < len(self.sample_points))

    def test_filter_noise(self):
        filtered_points = filter_noise(self.sample_points)
        self.assertTrue(len(filtered_points) <= len(self.sample_points))

if __name__ == "__main__":
    unittest.main()
