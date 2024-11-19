import os
from src.utils import load_point_cloud, save_point_cloud
from src.preprocess import normalize_point_cloud, voxel_grid_downsample, filter_noise

def preprocess_point_clouds(input_dir, output_dir):
    """
    Processes multiple point cloud files from an input directory and saves the results to an output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the output directory if it doesn't exist

    # List all files in the input directory
    files = [f for f in os.listdir(input_dir) if f.endswith('.pcd') or f.endswith('.ply')]
    
    if not files:
        print("No point cloud files found in the input directory.")
        return
    
    for file_name in files:
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, f"processed_{file_name}")
        
        print(f"Processing file: {file_name}")
        points = load_point_cloud(input_path)
        print(f"Loaded {len(points)} points.")
        
        # Step 1: Normalize
        points = normalize_point_cloud(points)
        print("Point cloud normalized.")
        
        # Step 2: Noise Filtering
        points = filter_noise(points)
        print("Noise removed from point cloud.")
        
        # Step 3: Voxel Downsampling
        points = voxel_grid_downsample(points, voxel_size=0.1)
        print(f"Downsampled to {len(points)} points.")
        
        # Save processed data
        save_point_cloud(points, output_path)
        print(f"Saved processed file to {output_path}.\n")

if __name__ == "__main__":
    raw_data_dir = "data/raw/"
    processed_data_dir = "data/processed/"
    preprocess_point_clouds(raw_data_dir, processed_data_dir)
