import subprocess
from pathlib import Path


def create_parameters_set(default_parameters_set, lpath, rpath):
    
    parameter_sets = []
    for item in lpath:
        if item.is_file():
            new_param_set = default_parameters_set.copy()
            new_param_set[3] = str(item)
            parameter_sets.append(new_param_set)
    count = 0
    for item in rpath:
        if item.is_file():
            parameter_sets[count][5] = str(item)
            count += 1
    return parameter_sets 
                     
        
def main(left_folder_path, right_folder_path, output_path):
    default_parameters_set =
    ["--model_dir", "Fast-FoundationStereo/weights/23-36-37/model_best_bp2_serialize.pth", "--left_file", 
    "processed_images/left/L.1428247884.497861.png", "--right_file", 
    "processed_images/right/R.1428247884.497861.png",
    "--intrinsic_file", "processed_images/K.txt", "--out_dir", "output/", 
    "--remove_invisible", "0", "--denoise_cloud", "0", "--scale", "--get_pc", "1", 
    "--valid_iters", "8", "--max_disp", "192", "--zfar", "100"]
    left_path = Path(left_folder_path)
    right_path = Path(right_folder_path)
    left_file_count = sum(1 for item in left_path.iterdir() if item.is_file())
    right_file_count = sum(1 for item in right_path.iterdir() if item.is_file())
    assert(left_file_count == right_file_count)
    parameter_sets = create_parameters_set(default_parameters_set, left_path, right_path)
    for params in parameter_sets:
        print(f"Running script with arguments: {params}")
        command = ["python", "Fast-FoundationStero/scripts/run_demo.py"] + params
        subprocess.run(command, check=True)
    print("All command iterations completed.")
        
if __name__ == "__main__":
    main()