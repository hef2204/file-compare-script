import os
import filecmp
from PIL import Image

file1 = input("Enter the path to the first file: ")
file2 = input("Enter the path to the second file: ")


def compare_files(file1, file2):

    def compare_images(file1, file2):
        img1 = Image.open(file1)
        img2 = Image.open(file2)
        if list(img1.getdata()) == list(img2.getdata()):
            print("Images are the same")
        else:
            print("Images are different")


    def compare_archives(file1, file2):
        if  os.path.getsize(file1) == os.path.getsize(file2):
            print("Archive files are the same")
        else:
            print("Archive files are different")

    def compare_text_files(file1, file2):
        if filecmp.cmp(file1, file2, shallow=False):
            print("Files are the same")
        else:
            print("Text files are different")

    comparisons = {
        '.jpg': compare_images,
        '.png': compare_images,
        '.jpeg': compare_images,
        '.zip': compare_archives,
        '.tar': compare_archives,
        '.txt': compare_text_files,
    }

    ext = os.path.splitext(file1)[1]
    if ext in comparisons:
        return comparisons[ext](file1, file2)
    else:
        print("Files are different")


compare_files(file1, file2)
