import numpy as np
import open3d as o3d

def load_point_cloud(file_path):
    """Loads point cloud data from a file."""
    pcd = o3d.io.read_point_cloud(file_path)
    return np.asarray(pcd.points)

def save_point_cloud(points, file_path):
    """Saves point cloud data to a file."""
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.io.write_point_cloud(file_path, pcd)
