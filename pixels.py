import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os
from PIL import Image
import pandas as pd

def intensidad_pixels(folder_path):
    # Extrae la intensidad de los pixeles de las fotos y los guarda en un archivo csv
    # 0 representa un pixel completamente negro
    # 255 representa un pixel completamente blanco

    # Get a list of file names in the folder
    file_names = os.listdir(folder_path)


    all_greyscale_values = []

    # Iterate over the file names
    for file_name in file_names:
        # Construct the file path
        file_path = os.path.join(folder_path, file_name)
        
        # Load the image using PIL
        image = Image.open(file_path)
        
        # Convert the image to greyscale
        image = image.convert('L')
        
        # Resize the image to 30x30 pixels
        image = image.resize((30, 30))
        
        # Convert the image to a numpy array
        image_array = np.array(image)
        
        # Extract the greyscale values for each pixel
        greyscale_values = image_array.flatten()
        
        # Append the file name and the greyscale values as a single row
        all_greyscale_values.append([file_name] + greyscale_values.tolist())
        
    
    # Create a DataFrame to store all the greyscale values
    df = pd.DataFrame(all_greyscale_values)

    # Save the DataFrame to a CSV file
    df.to_csv('greyscale_values.csv', index=False) # Este archivo tiene todos los valores de los pixeles de las fotos
