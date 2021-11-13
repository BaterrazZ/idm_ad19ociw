import numpy as np
from ipywidgets import interact, fixed
from PIL import Image


# How can I pass an array to the. interact function?


def imshow(X, resize=None):
    # def plot_Im(Im, resize):
    # Im = Im.resize(resize)
    # display(Im)
    # resize

    Img_1 = Image.fromarray(X)  # bring maximum value to 255, convert to pillow Image
    Img_1 = Img_1.resize(resize)
    return Img_1
    # interact(plot_Im(Img_1), resize = (100, 200,1000))
