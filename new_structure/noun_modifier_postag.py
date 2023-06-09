import os
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

# data path should lnclude in reformat_data_clean folder
clean_data_folder = r'D:\textmining lab demo\Assessment2\Assignment2BlogData\reformat_data_clean\male'

# output path should include in pos_data_strategy folder
output_folder = r'D:\textmining lab demo\Assessment2\Assignment2BlogData\pos_data_strategy\noun_modifier\male'

# initial lemmatizer
lemmatizer = WordNetLemmatizer()

# Iterate through each XML file
for file in os.listdir(clean_data_folder):
    if file.endswith('.txt'):
        clean_file = os.path.join(clean_data_folder, file)

        # read clean data
        with open(clean_file, 'r', encoding='utf-8') as f:
            data = f.read()

        # tokenization
        tokens = data.split()

        # POS Tag
        tagged_tokens = pos_tag(tokens)

        # set save list
        extracted_terms = []

        for i in range(len(tagged_tokens)):
            word, pos = tagged_tokens[i]

            if pos.startswith('NN'):  # start with 'NN'
                # lemmatization
                word = lemmatizer.lemmatize(word)

                # add to save list
                extracted_terms.append(word)

                # get last word
                prev_word, prev_pos = tagged_tokens[i - 1] if i > 0 else ('', '')

                if prev_pos.startswith('JJ'):  # start with 'JJ'
                    extracted_terms.append(prev_word + ' ' + word)

        # print result
        if extracted_terms:
            print('cleaned data file:', file)
            print('noun and modifier:', ', '.join(extracted_terms))
            print('-----------------------------')

            # set output
            output_file = os.path.join(output_folder, file.replace('.txt', '.txt'))

            # save data
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(' '.join(extracted_terms))

            print('saved file:', output_file)