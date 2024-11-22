import open3d as o3d

def visualize_meshes(meshes, point_cloud=None):
    print("Visualizing meshes...")
    geometries = meshes
    if point_cloud:
        geometries.append(point_cloud)
    o3d.visualization.draw_geometries(geometries, mesh_show_back_face=True)
