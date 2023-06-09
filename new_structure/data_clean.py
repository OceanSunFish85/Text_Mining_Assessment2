import re
import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# data path should include reformate_data folder
data_folder = 'new_structure/reformat_data/female'
output_folder = 'new_structure/reformat_data_clean/female'

# initial stopword and stemmer
stopwords = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

# regular pattern
punctuation_pattern = r'[^\w\s]'
repeated_chars_pattern = r'(.)\1{2,}'
url_link_pattern = r'\burllink\b'
meaningless_numbers_pattern = r'\b\d+\b'
non_english_words_pattern = r'[^\x00-\x7F]+'

# Iterate through each XML file
for file in os.listdir(data_folder):
    if file.endswith('.xml'):
        xml_file = os.path.join(data_folder, file)

        # load xml
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # extract date
        date = root.find('date').text

        # extract post
        post = root.find('post').text

        # clean html label and special label
        soup = BeautifulSoup(post, 'html.parser')
        clean_post = soup.get_text()

        # lower
        clean_post = clean_post.lower()

        # clean website address
        clean_post = re.sub(r'http\S+|www\S+', '', clean_post)

        # clean punctuation
        clean_post = re.sub(punctuation_pattern, ' ', clean_post)

        # clean non-alphanumeric characters
        clean_post = re.sub(r'\W+', ' ', clean_post)

        # clean urllink
        clean_post = re.sub(url_link_pattern, '', clean_post)

        # clean useless number
        clean_post = re.sub(meaningless_numbers_pattern, '', clean_post)

        # clean non english words
        clean_post = re.sub(non_english_words_pattern, '', clean_post)

        # clean bad words
        clean_post = re.sub(repeated_chars_pattern, '', clean_post)

        # clean stop word
        tokens = clean_post.split()
        tokens = [token for token in tokens if token not in stopwords]

        # stemmer
        stemmed_tokens = [stemmer.stem(token) for token in tokens]

        # judge post none or not
        if stemmed_tokens:
            # 打印清洗后的结果
            print('date:', date)
            print('cleaned post:', ' '.join(stemmed_tokens))
            print('-----------------------------')

            # create output path
        output_file = os.path.join(output_folder, file.replace('.xml', '.txt'))

        # save cleaned data
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(' '.join(tokens))

        print('saved file:', output_file)