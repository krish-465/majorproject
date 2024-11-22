import open3d as o3d
import numpy as np

def load_point_cloud(file_path):
    print(f"Loading point cloud from file: {file_path}")
    point_cloud = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)[:, :3]
    print(f"Loaded point cloud with {point_cloud.shape[0]} points.")
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_cloud)
    return pcd

def filter_noise(pcd, nb_neighbors=20, std_ratio=2.0):
    print("Filtering noise...")
    initial_point_count = len(pcd.points)
    pcd, _ = pcd.remove_statistical_outlier(nb_neighbors=nb_neighbors, std_ratio=std_ratio)
    final_point_count = len(pcd.points)
    print(f"Noise filtered: {initial_point_count - final_point_count} points removed. Remaining: {final_point_count}")
    return pcd

def remove_ground(pcd, distance_threshold=0.2):
    print("Removing ground points...")
    initial_point_count = len(pcd.points)
    _, inliers = pcd.segment_plane(distance_threshold=distance_threshold, ransac_n=3, num_iterations=1000)
    objects = pcd.select_by_index(inliers, invert=True)
    final_point_count = len(objects.points)
    print(f"Ground removed: {initial_point_count - final_point_count} points removed. Remaining: {final_point_count}")
    return objects

def downsample_point_cloud(pcd, voxel_size=0.05):
    print(f"Downsampling point cloud with voxel size: {voxel_size}")
    initial_point_count = len(pcd.points)
    pcd = pcd.voxel_down_sample(voxel_size)
    final_point_count = len(pcd.points)
    print(f"Downsampling completed: {initial_point_count - final_point_count} points removed. Remaining: {final_point_count}")
    return pcd
