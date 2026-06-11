import json
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
"Ozun": {"meanings":["dust"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Va": {"meanings":["claw"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Yara": {"meanings":["behold"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Mahk": {"meanings":["see","seeing"],"certainty_of_translation":"high","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Reh": {"meanings":["part","parting","apart"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Vome": {"meanings":["order"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun",],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Jahu": {"meanings":["form"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Ukul": {"meanings":["carapace","shell"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Ishlun": {"meanings":["dung"],"certainty_of_translation":"high","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Jass": {"meanings":["worm"],"certainty_of_translation":"high","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Ranac": {"meanings":["filled"],"certainty_of_translation":"high","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "adjective","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":""},
"Karis": {"meanings":["darkness"],"certainty_of_translation":"medium","source_of_translation":"Wiki users from-song translation","part_of_speech_tags": [],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka","Ris"], "compound_rule": "prefix + base","base_word": "Ris", "is_generated": False,"plural_form":"", "notes":""},



}


#{"meanings":[""],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": [],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "",  "is_generated": False,"plural_form":"", "notes":""},
# suffixes = {
# "suffixes_productive":{
#     "-hu": {"meanings": ["of-many","plentiful"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""}
# },    

# "suffixes_speculative":{
#     "-un": {"meanings": ["diminutive (?)"],"certainty_of_translation":"medium","source_of_translation":"wiki_official",  "attaches_to": ["noun", "adjective"], "notes":"Creator agrees with wiki official translation"}
# },
# "suffixes_unknown":{
#    "-tra": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},
#     "-li": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"}
# }
# }

# prefixes = {
# "prefixes_productive" :{
#   "Iv-": {"meanings": ["causative marker"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""}, 
#   "Ka-": {"meanings": ["inversion/'un-(X)'"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""},
#   "Sho-": {"meanings": ["Intensifier / 'Greater'"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""},
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