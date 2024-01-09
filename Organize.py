import os
import shutil

# -.exe, .gif, .png, .jpg, .jpeg, .csv, .pdf, .xls, .xlsx, .ppt, .pptx

from_dir = "C:\Users\Jorge A Rozo P\Downloads"
to_dir = "C:\Users\Jorge A Rozo P\Downloads\Imagenes_Archivos"

list_of_files = os.listdir(from_dir)


for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Imagenes_Archivos"
        path3 = to_dir + '/' + "Imagenes_Archivos" + '/' + file_name

#print("path1", path1)
#print("path3", path3)


#Verifica si la carpeta/directorio/ruta existe antes de moverla
#De lo contrario, haz una NUEVA carpeta/directorio luego muevela
if os.path.exists(path2):
    print("Moviendo" + file_name + ".....")

    #Mueve de path1 ---> path3
    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print("Moviendo" + file_name + ".....")
    shutil.move(path1, path3)