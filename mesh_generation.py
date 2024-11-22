import open3d as o3d
import numpy as np

def generate_convex_hull(cluster_points):
    if len(cluster_points) < 3:
        print("Not enough points to form a convex hull.")
        return None

    try:
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(cluster_points)
        hull, _ = pcd.compute_convex_hull()
        return hull
    except Exception as e:
        print(f"Error generating convex hull: {e}")
        return None

def generate_meshes(pcd, labels):
    print("Generating meshes for objects...")
    points = np.asarray(pcd.points)
    meshes = []

    for cluster_id in range(labels.max() + 1):
        cluster_points = points[labels == cluster_id]
        print(f"Processing cluster {cluster_id} with {len(cluster_points)} points.")
        
        if len(cluster_points) < 200:
            print(f"Skipping cluster {cluster_id} (too few points).")
            continue
        if len(cluster_points) > 5000:
            print(f"Skipping cluster {cluster_id} (too many points).")
            continue

        mesh = generate_convex_hull(cluster_points)
        if mesh:
            meshes.append(mesh)
            print(f"Cluster {cluster_id}: Convex hull generated successfully.")
    return meshes
