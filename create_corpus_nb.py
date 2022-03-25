import glob
import pandas as pd
import re
import pickle
from nltk import tokenize

# by KD
# Alle Entities in handannotierten Texten finden
# todo redundanten Code zu Funktionen zusammenfassen

filelist = glob.glob("./data_in/*.csv")
print("The following files were found: \n")
print(filelist)

for file in filelist:
    f = open(file, encoding="ansi")
    print(file + "has been opened ")
    full_text = pd.read_csv(f, delimiter=";")
    f.close()

    full_text_passage = full_text.filter(["Passage"])
    full_text_passage.to_csv("test.csv")

f = open("test.csv", encoding="utf-8")
full_text_string = f.read()
f.close()

# ############## Entities 1########################

entities_1 = re.findall("<e1>.*</e1>", full_text_string)
# print(entities_1)

entity1_list = []
for entity1 in entities_1:
    entity1_hv = entity1.replace("<e1>", "")
    entity1_hv2 = entity1_hv.replace("</e1>", "")
    entity1_list.append(entity1_hv2)
# print(entity1_list)

file_out = open("e1_pos_ex.csv", "w", encoding="utf-8")
for item in entity1_list:
    file_out.write(item + "\n")

# ############### Entities 2###########################

entities_2 = re.findall("<e2>.*</e2>", full_text_string)
# print(entities_2)

entity_list = []
for entity in entities_2:
    entity_hv = entity.replace("<e2>", "")
    entity_hv2 = entity_hv.replace("</e2>", "")
    entity_list.append(entity_hv2)
# print(entity_list)

file_out = open("e2_pos_ex.csv", "w", encoding="utf-8")
for item in entity_list:
    file_out.write(item + "\n")

# ##################### Relations ########################

relations = re.findall("<rel>.*</rel>", full_text_string)
# print(relations)

relation_list = []
for relation in relations:
    relation_hv = relation.replace("<rel>", "")
    relation_hv2 = entity_hv.replace("</rel>", "")
    relation_list.append(relation_hv2)
# print(relation_list)

file_out = open("rel_pos_ex.csv", "w", encoding="utf-8")
for item in relation_list:
    file_out.write(item + "\n")

# ############### Negativbeispiele ########################
# todo matcht jetzt das Richtige, ich lass das jetzt erstmal so
# todo aber es gibt bestimmt eine flag, die ich für non-greedy setzen kann
# todo dann können die ganzen zusätzlichen ? raus


neg_ex = re.findall("</.??e.??>.+?<.??e.??>", full_text_string)
print(neg_ex)

"""
neg_ex_list = []
for ex in neg_ex:
    neg_ex_hv = ex.replace("/>", "")
    neg_ex_hv2 = entity_hv.replace("<", "")
    neg_ex_list.append(neg_ex_hv2)
# print(neg_ex_list)

file_out = open("neg_ex.csv", "w", encoding="utf-8")
for neg_item in neg_ex_list:
    file_out.write(neg_item + "\n")

"""


# pickle.dump(entity_list, "e2.dmp", "w")

# filename = glob.glob("./data_out/NB_Corpus/*.txt")





