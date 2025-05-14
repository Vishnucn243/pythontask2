import os
def fun(directory, pattern="file", extension="txt"):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for index, filename in enumerate(files, start=1):
        new_name = f"{pattern}_{index}.{extension}"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)
        os.rename(src, dst)
        print(f"Renamed '{filename}' to '{new_name}'")

directory_path = "filesname"
fun(directory_path, pattern="document", extension="txt")
