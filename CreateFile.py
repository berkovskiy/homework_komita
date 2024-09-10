import os
import zipfile

num_files = 800
file_size = 120 * 1024  # 120 Кб
temp_dir = 'temp_files'
zip_name = 'archive.zip'

if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

for i in range(num_files):
    file_path = os.path.join(temp_dir, f'file_{i+1}.txt')
    with open(file_path, 'wb') as file:
        file.write(b'\0' * file_size)

with zipfile.ZipFile(zip_name, 'w') as zipf:
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, temp_dir))

for root, dirs, files in os.walk(temp_dir, topdown=False):
    for file in files:
        os.remove(os.path.join(root, file))
    for dir in dirs:
        os.rmdir(os.path.join(root, dir))

os.rmdir(temp_dir)

print(f'Архив "{zip_name}" успешно создан.')