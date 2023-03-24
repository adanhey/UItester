import os
import shutil


def del_pic():
    for root, dirs, files in os.walk("./"):
        for dice in dirs:
            if 'mission' in str(dice):
                shutil.rmtree(str(dice))


def del_log():
    for root, dirs, files in os.walk("./"):
        for file in files:
            if 'testLog' in str(file):
                os.remove(file)


if __name__ == "__main__":
    del_log()
    del_pic()

