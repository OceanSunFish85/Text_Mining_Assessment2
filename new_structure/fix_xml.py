import os
import re
from bs4 import BeautifulSoup
from lxml import etree

#define process function
def process_xml_file(file_path):
    try:
        # load xml
        with open(file_path, 'r', encoding='latin-1') as file:
            xml_content = file.read()

        # create beautifulsoup object
        soup = BeautifulSoup(xml_content, 'lxml-xml')

        # handling undefined entity references
        for element in soup.find_all(text=lambda text: re.search(r'&(?!(amp|lt|gt|quot|apos);)', text)):
            element.replace_with(re.sub(r'&(?!(amp|lt|gt|quot|apos);)', '&amp;', str(element)))

        # save file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

        print(f"processed file: {file_path}")
    except FileNotFoundError:
        print(f"not found: {file_path}")
    except Exception as e:
        print(f"process error: {file_path}")
        print(f"Error message: {str(e)}")

# xml file should clean original data
xml_directory = r'D:\textmining lab demo\Assessment2\Assignment2BlogData\blogs'

# Iterate through each XML file
for filename in os.listdir(xml_directory):
    if filename.endswith('.xml'):
        file_path = os.path.join(xml_directory, filename)
        process_xml_file(file_path)
