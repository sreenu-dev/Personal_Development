import os
import shutil

def get_folder_names(folder):
    folder_names = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    return folder_names

def count_files_in_folder(folder):
    file_count = 0
    for root, _, files in os.walk(folder):
        file_count += len(files)
    return file_count

def extract_files(source_folders, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    total_count=0
    for folder in source_folders:
        # Check if the source folder exists
        if not os.path.exists(folder):
            print(f"Source folder does not exist: {folder}")
            continue
        print("Count of Folder:"+folder+" is "+str(count_files_in_folder(folder)))
        total_count=total_count+count_files_in_folder(folder)
        for root, _, files in os.walk(folder):
            for file in files:
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_folder, file)

                # Copy the file to the destination folder
                shutil.copy2(source_file, destination_file)
                print(f"Copied {source_file} to {destination_file}")
    print("Total Files Extracted:"+str(total_count))
if __name__ == "__main__":
    # List of source folders to extract files from
    source_folders = []
    takeOutFolder='C:/TakeOutSet/takeout-20241114T064952Z-001/Takeout/Google Photos'
    # Destination folder to store the extracted files
    destination_folder = 'C:/TakeOutSet/takeout-20241114T064952Z-001/Takeout/Google Photos/All'

    # extract_files(source_folders, destination_folder)
    # print("Total Files Extracted:"+str(total_count))
    folders_in_takeout=get_folder_names(takeOutFolder)
    print("Folder Names: "+str(get_folder_names(takeOutFolder)))
    for folder in folders_in_takeout:
        print("Count of Folder:"+folder+" is "+str(count_files_in_folder(takeOutFolder+'/'+folder)))
        source_folders.append(takeOutFolder+'/'+folder)
    print(source_folders)
    extract_files(source_folders, destination_folder)
    
    print("Total files in Newly extractedd: "+str(count_files_in_folder(destination_folder)))