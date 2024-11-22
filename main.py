import os
import open3d as o3d
from preprocessing import load_point_cloud, filter_noise, remove_ground, downsample_point_cloud
from clustering import segment_objects_by_radius
from mesh_generation import generate_meshes
from visualization import visualize_meshes
from utils import ensure_folder, get_files_in_folder

def process_point_cloud(file_path, output_folder):
    print(f"Processing: {file_path}")
    ensure_folder(output_folder)

    # Step 1: Preprocessing
    pcd = load_point_cloud(file_path)
    pcd = filter_noise(pcd)
    objects = remove_ground(pcd)

    # Optional: Downsample
    objects = downsample_point_cloud(objects, voxel_size=0.1)

    # Step 2: Clustering
    labels, clustered_pcd = segment_objects_by_radius(objects, eps=2.0, min_samples=10)
    clustered_pcd_path = os.path.join(output_folder, "clustered_pcd.ply")
    o3d.io.write_point_cloud(clustered_pcd_path, clustered_pcd)

    # Step 3: Mesh Generation
    meshes = generate_meshes(clustered_pcd, labels)
    for i, mesh in enumerate(meshes):
        mesh_path = os.path.join(output_folder, f"mesh_cluster_{i}.ply")
        o3d.io.write_triangle_mesh(mesh_path, mesh)

    # Optional Visualization
    # visualize_meshes(meshes, point_cloud=objects)

if __name__ == "__main__":
    INPUT_FOLDER = "./input/"
    OUTPUT_FOLDER = "./output/"

    ensure_folder(INPUT_FOLDER)
    ensure_folder(OUTPUT_FOLDER)

    files = get_files_in_folder(INPUT_FOLDER)
    for file_path in files:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        output_folder = os.path.join(OUTPUT_FOLDER, file_name)
        ensure_folder(output_folder)
        process_point_cloud(file_path, output_folder)
