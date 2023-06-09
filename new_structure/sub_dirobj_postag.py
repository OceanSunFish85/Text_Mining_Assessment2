import os
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

# data path should include in reformat_data_clean folder
clean_data_folder = r'D:\textmining lab demo\Assessment2\Assignment2BlogData\reformat_data_clean\male'

# output path
output_folder = r'D:\textmining lab demo\Assessment2\Assignment2BlogData\pos_data_strategy\sub_dir_obj\male'

# lemmatizer
lemmatizer = WordNetLemmatizer()

# Iterate through each XML file
for file in os.listdir(clean_data_folder):
    if file.endswith('.txt'):
        clean_file = os.path.join(clean_data_folder, file)

        # load file
        with open(clean_file, 'r', encoding='utf-8') as f:
            data = f.read()

        # tokenization
        tokens = data.split()

        # POS Tag
        tagged_tokens = pos_tag(tokens)

        # data save list
        extracted_subjects = []
        extracted_direct_objects = []

        for i in range(len(tagged_tokens)):
            word, pos = tagged_tokens[i]

            if pos == 'NNP':  # start with 'NNP'
                # lemmatization
                word = lemmatizer.lemmatize(word)

                # if not null
                if word:
                    extracted_subjects.append(word)

            if pos == 'NN':  # start with 'NN'
                # lemmatization
                word = lemmatizer.lemmatize(word)

                # if nut null
                if word:
                    extracted_direct_objects.append(word)

        # print result
        if extracted_subjects or extracted_direct_objects:
            print('清洗后的数据文件:', file)
            print('提取的主语:', ', '.join(extracted_subjects))
            print('提取的直接宾语:', ', '.join(extracted_direct_objects))
            print('-----------------------------')

            # create output path
            output_file = os.path.join(output_folder, file.replace('.txt', '.txt'))

            # save to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(' '.join(extracted_subjects + extracted_direct_objects))

            print('saved file:', output_file)
