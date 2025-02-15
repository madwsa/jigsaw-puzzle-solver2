from os import listdir, path
from PIL import Image
from os.path import isfile, join, splitext
import pandas as pd

def set_size(width, fraction=1, subplots=(1, 1)):
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string
            Document width in points, or string of predined document type
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if width == 'thesis':
        width_pt = 426.79135
    elif width == 'beamer':
        width_pt = 307.28987
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    # https://disq.us/p/2940ij3
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)

def get_info(data_path):
    # load file names train dataset
    file_names = [splitext(f)[0] for f in listdir(data_path) if isfile(join(data_path, f))]

    # load file name test dataset
    #file_names_test = [splitext(f)[0] for f in listdir(data_path_test) if isfile(join(data_path_test, f))]

    # Split the image naming in wirter, page and fragment
    # For training
    #file_names_parts = [i.split("_") for i in file_names]
    # For test
    file_names_parts = [i.split("_") for i in file_names]

    return pd.DataFrame.from_records(file_names_parts,columns=['writer_id', 'page_id','fragment_id'])

def get_filenames(train_path, test_path):
    # load file names train dataset
    train = [path.splitext(f)[0] for f in listdir(train_path) if path.isfile(path.join(train_path, f))]

    # load file name test dataset
    test = [path.splitext(f)[0] for f in listdir(test_path) if path.isfile(path.join(test_path, f))]
    return train, test

def get_imgsize(train_filenames, test_filenames, train_path, test_path):
    train = [Image.open(train_path + '/' +f+ '.jpg', 'r').size for f in train_filenames]
    test = [Image.open(test_path + '/'+ f + '.jpg', 'r').size for f in test_filenames]
    return train, test