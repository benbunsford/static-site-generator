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
                shutil.copy(source_path, destination_path)

    source_dir = "static"
    destination_dir = "docs"
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)
    copy_tree(source_dir, destination_dir)
