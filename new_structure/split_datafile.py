import os
import shutil

# data path should include in fixed of original blog data set
source_folder = r"D:\textmining lab demo\Assessment2\Assignment2BlogData\blogs_v1"

# target data
male_folder = r"D:\textmining lab demo\Assessment2\Assignment2BlogData\reformat_data\male"
female_folder = r"D:\textmining lab demo\Assessment2\Assignment2BlogData\reformat_data\female"

# Iterate through each XML file
for filename in os.listdir(source_folder):
    # extract gender
    gender = filename.split(".")[1]

    # data path
    source_file = os.path.join(source_folder, filename)

    # target folder
    target_folder = male_folder if gender == "male" else female_folder

    # target path
    target_file = os.path.join(target_folder, filename)

    # create folder if not exist
    os.makedirs(target_folder, exist_ok=True)

    # remove file
    shutil.move(source_file, target_file)

print("file classifaction done")
