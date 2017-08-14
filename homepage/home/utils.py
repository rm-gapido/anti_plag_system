#import packages
import io
from PIL import Image 
import pytesseract
from wand.image import Image as wi

from os import listdir, mkdir
from os.path import dirname, exists, isdir, realpath, isfile, join
from fpdf import FPDF

# Path for scanned files
SCANNED_FILES_DIR = dirname(realpath(__file__)) + "/Documents/"

def create_dir(folder_name):
    content = SCANNED_FILES_DIR + folder_name

    if exists(content):
        print('[ERROR] Folder already exists!')
        return False
    print('[SUCCESS] Folder createds')
    mkdir(content)
    return True

def remove_escape_char(str, esc_char):
    index = str.rfind(esc_char)
    return str[:index]

def read_from_image(img_path):
    # TODO:
    # Recode this block to read text from image file (OCR)
    # For mockup purposes, Im using simple txt file
    lines = []  # Temporary list each lines from file

    # Open file, and read its contents
    with open(img_path) as f:
        # Read file per line and append its content to templist
        lines = f.readlines()

    formatted_list = []
    for line in lines:
        formatted_list.append(remove_escape_char(line, '\n'))
    return formatted_list


def gen_pdf_from_dir(folder_name):
    folder_dir = SCANNED_FILES_DIR + folder_name

    # TODO: Add handling to retrieve image files only
    # For mockup purposes, Im retrieving all files under the folder_dir
    files = [f for f in listdir(folder_dir) if isfile(join(folder_dir, f))]

    file_contents = [] # List ng files
    # [
    #     [
    #         ["line1","line2", etc]
    #     ]

    # ] 
    for file in files:
        print(file)
        file_contents.append(read_from_image(folder_dir + '/' + file))

    # 

    print(file_contents[0])

    # print(len(file_contents))
    # convert_to_pdf(file_contents, folder_name)
