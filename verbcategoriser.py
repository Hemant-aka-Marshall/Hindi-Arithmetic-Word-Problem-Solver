# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from source import source, sentences
from isc_tokenizer import Tokenizer
from isc_tagger import Tagger
import os
from os import system
from list_of_verbs import verbname, verbtype

# ensures the question is split according to sentences
tk = Tokenizer(lang='hin', split_sen=True)
tagger = Tagger(lang='hin')
# parser = Parser(lang='hin')

counter = 0

y = []
for i in range(36, 39):
    y.append(sentences[i])


for i in sentences:
    # Stores the list of seperated sentences within a question
    sep_sentence = tk.tokenize(i)
    # Stores the corresponding tags
    tag_sep_sent = []
    values = []
    containers = []
    objects = []
    for j in sep_sentence:
        print(j)
        for words in j:
            # print(words)
            tags = tagger.tag(words.split())
            # print(tags)
            # tags[0] = tags[0].split()
            if(tags[0][1] == 'VM'):
                os.system("touch output.txt")
                f = open('tempfile.txt', 'w+', encoding='utf-8')
                flag = 0
                f.write(tags[0][0])
                os.system(
                    "python3 run_morph_on_file_with_raw_text.py --input tempfile.txt --output output.txt")
                f2 = open('output.txt', 'r', encoding='utf-8')
                data = f2.read()
                data = data.replace(',', ' ')
                data = data.replace("'", ' ')
                data = data.split()
                l = len(data)
                for x in range(l):
                    if(data[x] == "af="):
                        stem = data[x+1]
                        print(stem)
                        if(stem in verbname):
                            ind = verbname.index(stem)
                            print(ind)
                            print(verbtype[ind])
                            flag = 1
                            break
                if flag == 0:
                    print("0")
                os.system("rm output.txt")

                f2.close()