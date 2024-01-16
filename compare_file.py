import filecmp
import os
from PIL import Image



def Compare_files(file_path1, file_path2):
    try:
        if os.path.splitext(file_path1)[1] in ['.jpg', '.png', '.jpeg']:  
            img1 = Image.open(file_path1)
            img2 = Image.open(file_path2)
            if list(img1.getdata()) == list(img2.getdata()):
                print("Images are the same")
            else:
                print("Images are different")

        elif os.path.splitext(file_path1)[1] in ['.zip']:  
            size1 = os.path.getsize(file_path1)
            size2 = os.path.getsize(file_path2)
            if size1 == size2:
                print("Zip files are the same size")
            else:
                print("Zip files are different sizes")

        elif os.path.splitext(file_path1)[1] in ['.tar']:  
            size1 = os.path.getsize(file_path1)
            size2 = os.path.getsize(file_path2)
            if size1 == size2:
                print("Tar files are the same size")
            else:
                print("Tar files are different sizes")

        elif os.path.splitext(file_path1)[1] in ['.txt']:
            if filecmp.cmp(file_path1, file_path2, shallow = False):
                print("Files are the same")
            else:
                print("Text files are different")
        else:
            print("Files are different")
    except FileNotFoundError:
        print("File not found")


    




def Compare_directories(dir_path1, dir_path2):
    try:
        directory_cmp = filecmp.dircmp(dir_path1, dir_path2)
        print("Files only in", dir_path1, ":", directory_cmp.left_only)
        # print("Files only in", dir_path2, ":", directory_cmp.right_only)

        for file in directory_cmp.common_files:
            path1 = os.path.join(dir_path1, file)
            path2 = os.path.join(dir_path2, file)
            if Compare_files(path1, path2):
                print(f"File {file} is the same in both directories")
            else:
                print(f"File {file} is different between the two directories")
    except FileNotFoundError:
        print("Directory not found")


def main():
    while True:
        print("1. Compare files")
        print("2. Compare directories")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            file_path1 = input("Enter the path of the first file: ")
            file_path2 = input("Enter the path of the second file: ")
            Compare_files(file_path1, file_path2)

        elif choice == '2':
            dir_path1 = input("Enter the path of the first directory: ")
            dir_path2 = input("Enter the path of the second directory: ")
            Compare_directories(dir_path1, dir_path2)
        elif choice == '3':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()









    







    


    