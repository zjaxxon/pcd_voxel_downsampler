import open3d as o3d
import sys

def downsample_point_cloud(input_file, output_file, voxel_size=0):
    # Load the point cloud
    pcd = o3d.io.read_point_cloud(input_file)
    if voxel_size == 0:
        min_bound = pcd.get_min_bound()
        max_bound = pcd.get_max_bound()
        ranges = max_bound - min_bound

        # Heuristic: set voxel size to 1% of the point cloud's spatial extent
        voxel_size = 0.01 * max(ranges)
        print(f'Set voxel size {voxel_size}')

    # Print the original number of points
    print(f'Point cloud has {len(pcd.points)} points before downsampling')

    # Apply voxel downsampling
    downsampled_pcd = pcd.voxel_down_sample(voxel_size=voxel_size)

    # Print the number of points after downsampling
    print(f'Point cloud has {len(downsampled_pcd.points)} points after downsampling')

    # Save the downsampled point cloud
    o3d.io.write_point_cloud(output_file, downsampled_pcd, write_ascii=True)

    print(f'Downsampled point cloud saved to {output_file}')


if __name__ == "__main__":
    if len(sys.argv) == 3:
        voxel_size = 0
    elif len(sys.argv) == 4:
        voxel_size = sys.argv[3]
    else:
        print("Usage: python downs.py input output voxel_size")
        exit()

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    downsample_point_cloud(input_path, output_path, int(voxel_size))
