import zipfile
import os
import rarfile

def create_archive(source_folder, destination_folder, zip_filename):
    try:
        zip_path = os.path.join(destination_folder, zip_filename)
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(source_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=file_path[len(source_folder) + 1:]) # Отсутствие относительного пути
        print(f"Archive created: {zip_path}")
    except FileNotFoundError:
        print(f"Folder {source_folder} did not found.")
    except Exception as e:
        print(f"Error on creating archive: {e}")

s = input()

source_folder = "путь_к_вашей_папке"
destination_folder = "путь_к_папке_для_архива"
zip_filename = "мой_архив.zip"

if "ME" in s:
    create_archive(source_folder + "CAS_ME//", destination_folder, zip_filename)
elif "API" in s:
    create_archive(source_folder + "CAS_APIS//", destination_folder, zip_filename)


