import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import open3d as o3d

def segment_objects_by_radius(pcd, eps=0.5, min_samples=10):
    print("Segmenting objects by radius...")
    points = np.asarray(pcd.points)
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(points)
    labels = clustering.labels_

    max_label = labels.max()
    print(f"Found {max_label + 1} clusters")
    colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0  # Noise points in black
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    return labels, pcd
