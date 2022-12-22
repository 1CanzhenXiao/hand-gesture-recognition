import os

path = 'RESIZED_DATASET'
dirs = os.listdir(path)
num_dir = len(dirs)
for i in range(num_dir):
    dir_path = os.path.join(path, str(i))
    pngs = os.listdir(dir_path)
    num_png = len(pngs)
    # print(pngs)
    for j in range(num_png):
        file_name = f'{i}_{j}.png'
        old_file = os.path.join(dir_path, pngs[j])
        new_file = os.path.join(dir_path, file_name)
        os.rename(old_file, new_file)
