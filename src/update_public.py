import os
import shutil

def update_public():
    def copy_tree(source_dir, destination_dir):
        static_items = os.listdir(source_dir)
        for item in static_items:
            source_path = os.path.join(source_dir, item)
            destination_path = os.path.join(destination_dir, item)
            if os.path.isdir(source_path):
                os.mkdir(destination_path)
                copy_tree(source_path, destination_path)
            else:
                print(item)
                shutil.copy(source_path, destination_path)

    cwd = os.getcwd()
    source_dir = os.path.join(cwd, "static")
    destination_dir = os.path.join(cwd, "public")
    print(cwd)
    print(source_dir)
    print(destination_dir)
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)
    copy_tree(source_dir, destination_dir)
