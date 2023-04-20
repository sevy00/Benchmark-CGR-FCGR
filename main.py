from PIL import Image
import os

import cv2
import numpy as np

if __name__ == '__main__':
    folder = 'F:/TirocinioSeverino/Dataset_Secondo/Dataset_Img/R.1'
    dest = 'F:/TirocinioSeverino/Dataset_Secondo/Dataset_Img_Resize/R.1'

    # Dati i vertici del quadrato
    vertices = [(245, 175), (245, 1280), (1730, 1280), (1730, 175)]

    # Calcola le coordinate delle parti interne del quadrato
    x1, y1 = vertices[0]
    x2, y2 = vertices[2]

    png_files = [f for f in os.listdir(folder) if f.endswith('.png')]

    # Per ogni file PNG nella cartella
    for filename in png_files:
        # Carica l'immagine
        img = cv2.imread(os.path.join(folder, filename))

        # Taglia solo la parte interna del rettangolo
        cropped_img = img[y1:y2, x1:x2]

        # Salva l'immagine tagliata
        cv2.imwrite(os.path.join(dest, filename), cropped_img)

    for filename in os.listdir(dest):
        if filename.endswith('.png'):
            img = Image.open(os.path.join(dest, filename))
            # img = Image.open(os.path.join(folder, filename))
            img_resized = img.resize((500, 375), Image.ANTIALIAS)
            img_resized.save(os.path.join(dest, filename))