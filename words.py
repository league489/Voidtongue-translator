import json
import streamlit as st
known_words = {
"Lohk": {"meanings":["void"],"certainty_of_translation":"full","source_of_translation":"in_game_official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Lohk", "is_generated": False,"plural_form":"", "notes":""},
"Bok": {"meanings":["service","servitude","slave(?)"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Bok", "is_generated": False,"plural_form":"", "notes":"'Slave' meaning is not confirmed"},
"Grikh": {"meanings":["strength","strong"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Grikh", "is_generated": False,"plural_form":"", "notes":""},
"Vak":{"meanings":["desolation","desolate"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Vak", "is_generated": False,"plural_form":"", "notes":""},
"Fass": {"meanings":["chaos"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Fass", "is_generated": False,"plural_form":"", "notes":""},
"Ris": {"meanings":["light"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ris", "is_generated": False,"plural_form":"", "notes":""},
"Oth": {"meanings":["gift","give","offer"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","verb"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Oth", "is_generated": False,"plural_form":"", "notes":""},
"Khra": {"meanings":["time"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Khra", "is_generated": False,"plural_form":"", "notes":""},
"Oull": {"meanings":["possibility"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Oull", "is_generated": False,"plural_form":"", "notes":""},
"Xata": {"meanings":["truth"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Xata", "is_generated": False,"plural_form":"", "notes":""},
"Ozun": {"meanings":["dust"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ozun", "is_generated": False,"plural_form":"", "notes":""},
"Va": {"meanings":["claw"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Va", "is_generated": False,"plural_form":"", "notes":""},
"Yara": {"meanings":["behold"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Yara", "is_generated": False,"plural_form":"", "notes":""},
"Mahk": {"meanings":["see","seeing","behold(?)"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","verb"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Mahk", "is_generated": False,"plural_form":"", "notes":"Wiki mentions 2 words with 'Behold' meaning. It's not certain which one is correct..."},
"Reh": {"meanings":["part","parting","apart"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","verb","adjective"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Reh", "is_generated": False,"plural_form":"", "notes":""},
"Vome": {"meanings":["order"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Vome", "is_generated": False,"plural_form":"", "notes":""},
"Jahu": {"meanings":["form"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Jahu", "is_generated": False,"plural_form":"", "notes":""},
"Ukul": {"meanings":["carapace","shell"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ukul", "is_generated": False,"plural_form":"", "notes":""},
"Ishlun": {"meanings":["dung"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ishlun", "is_generated": False,"plural_form":"", "notes":""},
"Jass": {"meanings":["worm"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Jass", "is_generated": False,"plural_form":"", "notes":""},
"Ranac": {"meanings":["filled(?)"],"certainty_of_translation":"medium","source_of_translation":"wiki official","part_of_speech_tags": ["adjective"],"default_part_of_speech": "adjective","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ranac", "is_generated": False,"plural_form":"", "notes":"Not confirmed , but assumed true in face of no alternatives"},
"Karis": {"meanings":["darkness"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka","Ris"], "compound_rule": "prefix + base","base_word": "Ris", "is_generated": False,"plural_form":"", "notes":""},
"Uubok": {"meanings":["eternal service"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["adjective","noun"],"default_part_of_speech": "ambiguous","is_compound": True, "compound_components": ["Uu-","Bok"], "compound_rule": "prefix + base","base_word": "Bok",  "is_generated": False,"plural_form":"", "notes":""},
"Vagithullah": {"meanings":["Has the X returned?"],"certainty_of_translation":"medium","source_of_translation":"wiki official","part_of_speech_tags": [],"default_part_of_speech": "ambigous","is_compound": True, "compound_components": ["Va-","Gith","Ullah"], "compound_rule": "(?)","base_word": "(?)",  "is_generated": False,"plural_form":"", "notes":"Va means 'claw', but the rest of compound components is unknown and it is hard to guess how they together create the final meaning"},
"Uuris": {"meanings":["eternal light"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Uu-","Ris"], "compound_rule": "prefix + base","base_word": "Ris",  "is_generated": False,"plural_form":"", "notes":""},
"Shotarat": {"meanings":["overlord","master"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["adjective","noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Sho-","Tarat"], "compound_rule": "prefix + base","base_word": "Tarat",  "is_generated": False,"plural_form":"", "notes":""},
"Tarat": {"meanings":["lord","ruler"],"certainty_of_translation":"medium","source_of_translation":"user_defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Tarat",  "is_generated": False,"plural_form":"", "notes":"Extracted from shotarat - as lord is lesser then overlord/master, I belive it makes sense"},
"Kalohk": {"meanings":["material world","world of dust"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Lohk"], "compound_rule": "prefix + base","base_word": "Lohk",  "is_generated": False,"plural_form":"", "notes":""},
"Shoranac": {"meanings":["Fill fiercely"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adverb"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Sho-","Ranac"], "compound_rule": "prefix + base","base_word": "Ranac",  "is_generated": False,"plural_form":"", "notes":""},
"Githli": {"meanings":["welcome","greeting"],"certainty_of_translation":"medium","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective","verb"],"default_part_of_speech": "ambiguous","is_compound": True, "compound_components": ["Gith","-li"], "compound_rule": "base + suffix","base_word": "Gith",  "is_generated": False,"plural_form":"", "notes":"Both suffix and base meanings are unknown , thus compound translation is questionable"},
"Uukareh": {"meanings":["eternal union","together forever"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Uu-","Ka-","Reh"], "compound_rule": "prefix + prefix + base","base_word": "Reh",  "is_generated": False,"plural_form":"", "notes":""},
"Shogrikh": {"meanings":["great strength(?)","stronger","stronger still"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "ambiguous","is_compound": True, "compound_components": ["Sho-","Grikh"], "compound_rule": "prefix + base","base_word": "Grikh",  "is_generated": False,"plural_form":"", "notes":"'Great strength' meaning has been added by me , it is not listed in wiki, but as 'strength' is one of 'Grikh' meaning, I found it important to add it."},
"Belia": {"meanings":["(Your) counterpart"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Bel","-ia"], "compound_rule": "base + suffix","base_word": "Bel",  "is_generated": False,"plural_form":"", "notes":"Both suffix and base meanings are unknown , thus compound translation is questionable"},
"Ivbok": {"meanings":["submit"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Bok"], "compound_rule": "prefix + base","base_word": "Bok",  "is_generated": False,"plural_form":"", "notes":""},
"Jeliira": {"meanings":["(My) heart"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Jeliira",  "is_generated": False,"plural_form":"", "notes":""},
"Mig": {"meanings":["newcomer"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Mig",  "is_generated": False,"plural_form":"", "notes":""},
"Sho": {"meanings":["continuous","still","more","most"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["adjective"],"default_part_of_speech": "adjective","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Sho",  "is_generated": False,"plural_form":"", "notes":"'Sho' is also an intensifing prefix"},
"Uu": {"meanings":["infinite","eternal","forever"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["adjective","noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Uu",  "is_generated": False,"plural_form":"", "notes":"'Uu' is also an 'eternal=(X)' prefix"},
"Kagrikh": {"meanings":["weak","weakness"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Grikh"], "compound_rule": "prefix + base","base_word": "Grikh",  "is_generated": False,"plural_form":"", "notes":""},
"Kaoth": {"meanings":["tribute","debt"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Oth"], "compound_rule": "prefix + base","base_word": "Oth",  "is_generated": False,"plural_form":"", "notes":"It is just a proposal, I am not sure if it even makes sense. Translation is open for discussion"},
"Kakhra": {"meanings":["timelessness","eternity"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Khra"], "compound_rule": "prefix + base","base_word": "Khra",  "is_generated": False,"plural_form":"", "notes":"It is just a proposal, I am not sure if it even makes sense. Translation is open for discussion"},
"Kaoull": {"meanings":["impossibility","fate"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Oull"], "compound_rule": "prefix + base","base_word": "Oull",  "is_generated": False,"plural_form":"", "notes":"The 'Oull' has no clear definiton of ''possibility' - is it single option? Space of countless options? "},
"Kaxata": {"meanings":["lie"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": [],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Xata"], "compound_rule": "prefix + base","base_word": "Xata",  "is_generated": False,"plural_form":"", "notes":""},
"Kaozun": {"meanings":["monolith","integrity"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": [], "compound_rule": "prefix + base","base_word": "Ozun",  "is_generated": False,"plural_form":"", "notes":"I have trouble with defining inversion/oppositon of dust, that is the most reasonable proposal i came up with"},
"Kareh": {"meanings":["united","together","union"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["adjective","noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Reh"], "compound_rule": "prefix + base","base_word": "Reh",  "is_generated": False,"plural_form":"", "notes":""},







}




#{"meanings":[""],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": [],"default_part_of_speech": "noun","is_compound": True, "compound_components": [], "compound_rule": "prefix + base","base_word": "",  "is_generated": False,"plural_form":"", "notes":""},

# suffixes = {
# "suffixes_productive":{
#     "-hu": {"meanings": ["of-many","plentiful"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""}
# },    

# "suffixes_speculative":{
#     "-un": {"meanings": ["diminutive (?)"],"certainty_of_translation":"medium","source_of_translation":"wiki_official",  "attaches_to": ["noun", "adjective"], "notes":"Creator agrees with wiki official translation"}
# },
# "suffixes_unknown":{
#    "-tra": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},
#     "-li": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},
#     "-ia": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},  
# }
# }

# prefixes = {
# "prefixes_productive" :{
#   "Iv-": {"meanings": ["causative marker"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""}, 
#   "Ka-": {"meanings": ["inversion/'un-(X)'"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""},
#   "Sho-": {"meanings": ["Intensifier / 'Greater'"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""},
#   "Uu-": {"meanings": ["Eternal-(X)"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""},
# },    

# "prefixes_unknown": {
#     "V-": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},
#     "Va-": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},
#     "Ko-(?)": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning, not confirmed if it even is a prefix"}
# }
        
# }


# conjunctions = {
# "conjunctions_productive":{
#     "Ra": {"meanings": ["from","out-of"],"certainty_of_translation":"medium","source_of_translation":"wiki_official", "type": "preposition", "structure": "X Ra Y", "notes":"No examples of use"},
#     "Khra": {"meanings": ["the time has come for X"],"certainty_of_translation":"medium","source_of_translation":"wiki_official", "type": "temporal_conjunction","structure": "Khra X", "notes":"No examples of use"}
# },

# "conjunctions_unknown":{
#  "Kah": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown", "type": "conjunction", "structure": "X Kah Y", "notes":"Lacks meaning"}   
# }

#  }


# pronouns = {
# "pronouns_known":{
#     "Veh": {"meanings": ["I am"],"type": "1st person copula","certainty_of_translation":"high","source_of_translation":"wiki_official", "grammatical_role": "subject","notes":""},
#     "Re-un": {"meanings": ["us","we"],"type": "1st person plural","certainty_of_translation":"high","source_of_translation":"wiki_official", "grammatical_role": "subject","notes":""}
# }
# }

# with open("prefixes.json",'w') as pref:
#     json.dump(prefixes,pref)
#     pref.close()

