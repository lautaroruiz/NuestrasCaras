import os
import cv2
import face_recognition
from PIL import Image   # para abrir imagenes HEIC


# Recorta las caras de cada imagen, las cambia a escala de grises y las guarda en una carpeta de salida

def cortar_imagenes(input_dir, output_dir):
    # Cargamos el detector de rostros de la libreria face_recognition
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    i = 0
    # Para cada archivo del directorio de imput comenzamos el loop
    for filename in os.listdir(input_dir):
        i += 1
        # Cargamos la imagen
        input_path = os.path.join(input_dir, filename)
        img = cv2.imread(input_path)

        # Detectamos el rostro en la imagen
        face_locations = face_recognition.face_locations(img)
        
        # Cortamos y cambiamos a escala de grises
        for (top, right, bottom, left) in face_locations:
            face = img[top:bottom, left:right]
            face = cv2.resize(face, (30, 30))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Guardamos el proceso en la carpeta de salida
            output_path = os.path.join(output_dir, f"{filename}")
            cv2.imwrite(output_path, face)




# Para copiar las imagenes de las carpetas individuales a una carpeta global

def copy_rename_images(input_dir, output_dir):
    # Iterate over each folder in the input directory
    for folder_name in os.listdir(input_dir):
        # Get the full path of the folder
        folder_path = os.path.join(input_dir, folder_name)
        # Check if the item in the input directory is a folder
        if os.path.isdir(folder_path):
            # Iterate over each file in the folder
            i = 0
            for filename in os.listdir(folder_path):
                i += 1
                # Get the full path of the file
                file_path = os.path.join(folder_path, filename)
                # Read the image
                img = cv2.imread(file_path)
                # Check if the image is loaded successfully
                if img is not None:
                    # Create the output folder if it doesn't exist
                    output_folder = os.path.join(output_dir)
                    os.makedirs(output_folder, exist_ok=True)
                    # Generate the new filename based on the folder name
                    new_filename = f"{folder_name}-{i}"+".jpg"
                    # Save the image with the new filename in the output folder
                    output_path = os.path.join(output_folder, new_filename)
                    cv2.imwrite(output_path, img)
                else:
                    print(f"Failed to load image: {file_path}")


#copy_rename_images("fotos_crudas", "input")

# Abrir imagenes .HEIC y transformar a .jpg  (REVISAR)

def heic_to_jpg(dir):
    for folder_name in os.listdir(dir):
        # Get the full path of the folder
        folder_path = os.path.join(dir, folder_name)
        # Iterate over each file in the input directory
        for filename in os.listdir(folder_path):
            # Get the full path of the file
            file_path = os.path.join(folder_path, filename)
            # Check if the file is an HEIC image
            if filename.endswith(".HEIC"):
                # Open the HEIC image using the PIL library
                img = Image.open(file_path)
                # Generate the output path with the same filename but a different extension
                output_path = os.path.join(dir, filename.replace(".HEIC", ".jpg"))
                # Save the image as a JPEG file
                img.save(output_path, "JPEG")


