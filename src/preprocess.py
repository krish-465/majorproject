import numpy as np
import open3d as o3d

def normalize_point_cloud(points):
    """
    Normalize point cloud data by centering and scaling.
    """
    centroid = np.mean(points, axis=0)
    points -= centroid  # Center the point cloud
    max_distance = np.max(np.linalg.norm(points, axis=1))
    points /= max_distance  # Scale the point cloud
    return points

def voxel_grid_downsample(points, voxel_size=0.1):
    """
    Downsample point cloud using voxel grid filtering.
    """
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    downsampled_pcd = pcd.voxel_down_sample(voxel_size=voxel_size)
    return np.asarray(downsampled_pcd.points)

def filter_noise(points, nb_neighbors=20, std_ratio=2.0):
    """
    Removes noise using statistical outlier removal.
    """
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=nb_neighbors, std_ratio=std_ratio)
    return np.asarray(pcd.select_by_index(ind).points)
