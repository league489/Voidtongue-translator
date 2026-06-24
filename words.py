import json
import streamlit as st
known_words = {
"Lohk": {"meanings":["void"],"certainty_of_translation":"full","source_of_translation":"in_game_official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Lohk", "is_generated": False,"plural_form":"Lohka", "notes":""},
"Bok": {"meanings":["service","servitude","slave(?)"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Bok", "is_generated": False,"plural_form":"Boka", "notes":"'Slave' meaning is not confirmed"},
"Grikh": {"meanings":["strength","strong"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Grikh", "is_generated": False,"plural_form":"Grikha", "notes":""},
"Vak":{"meanings":["desolation","desolate"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Vak", "is_generated": False,"plural_form":"Vaka", "notes":""},
"Fass": {"meanings":["chaos"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Fass", "is_generated": False,"plural_form":"Fassa", "notes":""},
"Ris": {"meanings":["light"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ris", "is_generated": False,"plural_form":"Risa", "notes":""},
"Oth": {"meanings":["gift","give","offer"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","verb"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Oth", "is_generated": False,"plural_form":"Otha", "notes":""},
"Khra": {"meanings":["time"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Khra", "is_generated": False,"plural_form":"Khraa", "notes":"'Khra' is also a conjunction, with 'the time has come for X' meening"},
"Oull": {"meanings":["possibility"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Oull", "is_generated": False,"plural_form":"Oulla", "notes":""},
"Xata": {"meanings":["truth"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Xata", "is_generated": False,"plural_form":"Xataa", "notes":""},
"Ozun": {"meanings":["dust"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ozun", "is_generated": False,"plural_form":"Ozuna", "notes":""},
"Va": {"meanings":["claw"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Va", "is_generated": False,"plural_form":"Vaa", "notes":""},
"Yara": {"meanings":["behold"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Yara", "is_generated": False,"plural_form":"", "notes":""},
"Mahk": {"meanings":["see","seeing","behold(?)"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","verb"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "", "is_generated": False,"plural_form":"", "notes":"Wiki mentions 2 words with 'Behold' meaning. It's not certain which one is correct..."},
"Reh": {"meanings":["part","parting","apart"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","verb","adjective"],"default_part_of_speech": "ambiguous","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Reh", "is_generated": False,"plural_form":"Reha", "notes":""},
"Vome": {"meanings":["order"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Vome", "is_generated": False,"plural_form":"Vomea", "notes":""},
"Jahu": {"meanings":["form"],"certainty_of_translation":"full","source_of_translation":"in-game official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Jahu", "is_generated": False,"plural_form":"Jahua", "notes":""},
"Ukul": {"meanings":["carapace","shell"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ukul", "is_generated": False,"plural_form":"Ukula", "notes":""},
"Ishlun": {"meanings":["dung"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ishlun", "is_generated": False,"plural_form":"Ishluna", "notes":""},
"Jass": {"meanings":["worm"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Jass", "is_generated": False,"plural_form":"Jassa", "notes":""},
"Ranac": {"meanings":["filled(?)"],"certainty_of_translation":"medium","source_of_translation":"wiki official","part_of_speech_tags": ["adjective"],"default_part_of_speech": "adjective","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Ranac", "is_generated": False,"plural_form":"", "notes":"Not confirmed , but assumed true in face of no alternatives"},
"Karis": {"meanings":["darkness"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka","Ris"], "compound_rule": "prefix + base","base_word": "Ris", "is_generated": False,"plural_form":"Karisa", "notes":""},
"Uubok": {"meanings":["eternal service"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["adjective","noun"],"default_part_of_speech": "ambiguous","is_compound": True, "compound_components": ["Uu-","Bok"], "compound_rule": "prefix + base","base_word": "Bok",  "is_generated": False,"plural_form":"Uuboka", "notes":""},
"Vagithullah": {"meanings":["Has the X returned?"],"certainty_of_translation":"medium","source_of_translation":"wiki official","part_of_speech_tags": [],"default_part_of_speech": "ambigous","is_compound": True, "compound_components": ["Va-","Gith","Ullah"], "compound_rule": "(?)","base_word": "(?)",  "is_generated": False,"plural_form":"", "notes":"Va means 'claw', but the rest of compound components is unknown and it is hard to guess how they together create the final meaning"},
"Uuris": {"meanings":["eternal light"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Uu-","Ris"], "compound_rule": "prefix + base","base_word": "Ris",  "is_generated": False,"plural_form":"Uurisa", "notes":""},
"Shotarat": {"meanings":["overlord","master"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["adjective","noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Sho-","Tarat"], "compound_rule": "prefix + base","base_word": "Tarat",  "is_generated": False,"plural_form":"Shotarata", "notes":""},
"Tarat": {"meanings":["lord","ruler"],"certainty_of_translation":"medium","source_of_translation":"user_defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Tarat",  "is_generated": False,"plural_form":"Tarata", "notes":"Extracted from shotarat - as lord is lesser then overlord/master, I belive it makes sense"},
"Kalohk": {"meanings":["material world","world of dust"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Lohk"], "compound_rule": "prefix + base","base_word": "Lohk",  "is_generated": False,"plural_form":"Kalohka", "notes":""},
"Shoranac": {"meanings":["fill fiercely"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adverb"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Sho-","Ranac"], "compound_rule": "prefix + base","base_word": "Ranac",  "is_generated": False,"plural_form":"", "notes":""},
"Githli": {"meanings":["welcome","greeting"],"certainty_of_translation":"medium","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective","verb"],"default_part_of_speech": "ambiguous","is_compound": True, "compound_components": ["Gith","-li"], "compound_rule": "base + suffix","base_word": "Gith",  "is_generated": False,"plural_form":"", "notes":"Both suffix and base meanings are unknown , thus compound translation is questionable"},
"Uukareh": {"meanings":["eternal union","together forever"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Uu-","Ka-","Reh"], "compound_rule": "prefix + prefix + base","base_word": "Reh",  "is_generated": False,"plural_form":"Uukareha", "notes":""},
"Shogrikh": {"meanings":["great strength(?)","stronger","stronger still"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "ambiguous","is_compound": True, "compound_components": ["Sho-","Grikh"], "compound_rule": "prefix + base","base_word": "Grikh",  "is_generated": False,"plural_form":"Shogrikha", "notes":"'Great strength' meaning has been added by me , it is not listed in wiki, but as 'strength' is one of 'Grikh' meaning, I found it important to add it."},
"Belia": {"meanings":["(Your) counterpart"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Bel","-ia"], "compound_rule": "base + suffix","base_word": "Bel",  "is_generated": False,"plural_form":"Beliaa", "notes":"Both suffix and base meanings are unknown , thus compound translation is questionable"},
"Ivbok": {"meanings":["submit"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Bok"], "compound_rule": "prefix + base","base_word": "Bok",  "is_generated": False,"plural_form":"", "notes":""},
"Jeliira": {"meanings":["(My) heart"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Jeliira",  "is_generated": False,"plural_form":"Jeliiraa", "notes":""},
"Mig": {"meanings":["newcomer"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Mig",  "is_generated": False,"plural_form":"Miga", "notes":""},
"Sho": {"meanings":["continuous","still","more","most"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["adjective"],"default_part_of_speech": "adjective","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Sho",  "is_generated": False,"plural_form":"", "notes":"'Sho' is also an intensifing prefix"},
"Uu": {"meanings":["infinite","eternal","forever"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["adjective","noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Uu",  "is_generated": False,"plural_form":"", "notes":"'Uu' is also an 'eternal=(X)' prefix"},
"Kagrikh": {"meanings":["weak","weakness"],"certainty_of_translation":"high","source_of_translation":"wiki official","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Grikh"], "compound_rule": "prefix + base","base_word": "Grikh",  "is_generated": False,"plural_form":"Kagrikha", "notes":""},
"Kaoth": {"meanings":["tribute","debt"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Oth"], "compound_rule": "prefix + base","base_word": "Oth",  "is_generated": False,"plural_form":"Kaotha", "notes":"It is just a proposal, I am not sure if it even makes sense. Translation is open for discussion"},
"Kakhra": {"meanings":["timelessness","eternity"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Khra"], "compound_rule": "prefix + base","base_word": "Khra",  "is_generated": False,"plural_form":"Kakhraa", "notes":"It is just a proposal, I am not sure if it even makes sense. Translation is open for discussion"},
"Kaoull": {"meanings":["impossibility","fate"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Oull"], "compound_rule": "prefix + base","base_word": "Oull",  "is_generated": False,"plural_form":"Kaoulla", "notes":"The 'Oull' has no clear definiton of ''possibility' - is it single option? Space of countless options? "},
"Kaxata": {"meanings":["lie"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": [],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Xata"], "compound_rule": "prefix + base","base_word": "Xata",  "is_generated": False,"plural_form":"Kaxataa", "notes":""},
"Kaozun": {"meanings":["monolith","integrity"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": [], "compound_rule": "prefix + base","base_word": "Ozun",  "is_generated": False,"plural_form":"Kaozuna", "notes":"I have trouble with defining inversion/oppositon of dust, that is the most reasonable proposal i came up with"},
"Kareh": {"meanings":["united","together","union"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["adjective","noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Reh"], "compound_rule": "prefix + base","base_word": "Reh",  "is_generated": False,"plural_form":"Kareha", "notes":""},
"Kajahu": {"meanings":["shapelessness","formlessness"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Jahu"], "compound_rule": "prefix + base","base_word": "Jahu",  "is_generated": False,"plural_form":"Kajahua", "notes":"Propably not very useful... but reasonable"},
"Kayara": {"meanings":["look away"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb","adverb"],"default_part_of_speech": "ambiguous","is_compound": True, "compound_components": ["Ka-","Yara"], "compound_rule": "prefix + base","base_word": "Yara",  "is_generated": False,"plural_form":"", "notes":""}, 
"Kamahk": {"meanings":["unsee","ignore"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Mahk"], "compound_rule": "prefix + base","base_word": "Mahk",  "is_generated": False,"plural_form":"", "notes":""},
"Kaukul": {"meanings":["interior","center"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Ukul"], "compound_rule": "prefix + base","base_word": "Ukul",  "is_generated": False,"plural_form":"Kaukula", "notes":""},
"Katarat": {"meanings":["subject","servant"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Tarat"], "compound_rule": "prefix + base","base_word": "Tarat",  "is_generated": False,"plural_form":"Katarata", "notes":""},
"Karanac": {"meanings":["depleted","empty"],"certainty_of_translation":"medium","source_of_translation":"user defined","part_of_speech_tags": ["adjective"],"default_part_of_speech": "adjective","is_compound": True, "compound_components": ["Ka-","Ranac"], "compound_rule": "prefix + base","base_word": "Ranac",  "is_generated": False,"plural_form":"", "notes":"As base word translation is uncertain, so is this compound's."},
"Kagithli": {"meanings":["goodbye"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Githli"], "compound_rule": "prefix + base","base_word": "Githli",  "is_generated": False,"plural_form":"", "notes":"It is just a proposal, I am not sure if it even makes sense. Translation is open for discussion"},
"Kaivbok":  {"meanings":["resist","defy"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Bok"], "compound_rule": "prefix + prefix + base","base_word": "Bok",  "is_generated": False,"plural_form":"", "notes":""},
"Kamig": {"meanings":["native","local"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["noun","adjective"],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Mig"], "compound_rule": "prefix + base","base_word": "Mig",  "is_generated": False,"plural_form":"Kamiga", "notes":""},
"Kasho": {"meanings":["discontinuos","variable","less","least"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": [],"default_part_of_speech": "noun","is_compound": True, "compound_components": ["Ka-","Sho"], "compound_rule": "prefix + base","base_word": "Sho",  "is_generated": False,"plural_form":"", "notes":""},
"Kauu": {"meanings":["finite","temporary","never"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["adjective","noun"],"default_part_of_speech": "ambiguous","is_compound": True, "compound_components": ["Ka-","Uu"], "compound_rule": "prefix + base","base_word": "Uu",  "is_generated": False,"plural_form":"", "notes":""},
"Voc": {"meanings":["voice"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "Voc",  "is_generated": False,"plural_form":"Voca", "notes":"Extracted from Voca - as game description describes Voca as 'voices/screams' , I deducted that Voc would be singular 'voice/scream'. Additionaly, it gave me an idea for plural noun suffix (-a), which I will use until I find more suitable replacement "},
"Mara":{"meanings":["devil","child"],"certainty_of_translation":"full","source_of_translation":"in-game translation","part_of_speech_tags": ["noun"],"default_part_of_speech": "noun","is_compound": False, "compound_components": [], "compound_rule": "","base_word": "",  "is_generated": False,"plural_form":"", "notes":""},
"Ivoth": {"meanings":["give","bestow"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Oth"], "compound_rule": "prefix + base","base_word": "Oth",  "is_generated": False,"plural_form":"", "notes":""},
"Ivmahk": {"meanings":["show","reveal"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Mahk"], "compound_rule": "prefix + base","base_word": "Mahk",  "is_generated": False,"plural_form":"", "notes":""},
"Ivyara": {"meanings":["summon","evoke"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Yara"], "compound_rule": "prefix + base","base_word": "Yara",  "is_generated": False,"plural_form":"", "notes":""},
"Ivreh": {"meanings":["separate","divide"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Reh"], "compound_rule": "prefix + base","base_word": "Reh",  "is_generated": False,"plural_form":"", "notes":""},
"Ivkhra": {"meanings":["cause to happen","initiate"],"certainty_of_translation":"low","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Khra"], "compound_rule": "prefix + base","base_word": "Khra",  "is_generated": False,"plural_form":"", "notes":"It comes from 'Khra' conjunction's meaning, I'm not sure if it is valid..."},
"Ivranac": {"meanings":["fill up","stuff"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Ranac"], "compound_rule": "prefix + base","base_word": "Ranac",  "is_generated": False,"plural_form":"", "notes":""},
"Ivukul": {"meanings":["encase","enshell"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Ukul"], "compound_rule": "prefix + base","base_word": "Ukul",  "is_generated": False,"plural_form":"", "notes":""},
"Ivjahu": {"meanings":["shape","form"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Jahu"], "compound_rule": "prefix + base","base_word": "Jahu",  "is_generated": False,"plural_form":"", "notes":""},
"Ivva": {"meanings":["claw","scratch"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Va"], "compound_rule": "prefix + base","base_word": "Va",  "is_generated": False,"plural_form":"", "notes":""},
"Ivgrikh": {"meanings":["strengthen","fortify"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Grikh"], "compound_rule": "prefix + base","base_word": "Grikh",  "is_generated": False,"plural_form":"", "notes":""},
"Ivris": {"meanings":["illuminate","enlight"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Ris"], "compound_rule": "prefix + base","base_word": "Ris",  "is_generated": False,"plural_form":"", "notes":""},
"Ivvome": {"meanings":["organize","oder"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Vome"], "compound_rule": "prefix + base","base_word": "Vome",  "is_generated": False,"plural_form":"", "notes":""},
"Ivozun": {"meanings":["pulverize","turn to dust"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Ozun"], "compound_rule": "prefix + base","base_word": "Ozun",  "is_generated": False,"plural_form":"", "notes":""},
"Ivkaris": {"meanings":["darken","overshadow"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Ka-","Ris"], "compound_rule": "prefix + prefix + base","base_word": "Ris",  "is_generated": False,"plural_form":"", "notes":""},
"Ivkalohk": {"meanings":["materialize","make real"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Ka-"], "compound_rule": "prefix + prefix + base","base_word": "Lohk",  "is_generated": False,"plural_form":"", "notes":""},
"Ivuu": {"meanings":["eternalize","make eternal"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-"], "compound_rule": "prefix + base","base_word": "",  "is_generated": False,"plural_form":"", "notes":""},
"Ivvoc": {"meanings":["vocalize","utter"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Voc"], "compound_rule": "prefix + base","base_word": "Voc",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivoth": {"meanings":["withold","take away"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Oth"], "compound_rule": "prefix + prefix + base","base_word": "Oth",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivmahk": {"meanings":["conceal","hide"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Mahk"], "compound_rule": "prefix + prefix + base","base_word": "Mahk",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivyara": {"meanings":["banish","dismiss"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Yara"], "compound_rule": "prefix + prefix + base","base_word": "Yara",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivreh": {"meanings":["unite","join"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Reh"], "compound_rule": "prefix + prefix + base","base_word": "Reh",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivgrikh": {"meanings":["weaken"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Grikh"], "compound_rule": "prefix + prefix + base","base_word": "Grikh",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivris": {"meanings":["darken","overshadow"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Iv-","Ka-","Ris"], "compound_rule": "prefix + prefix + base","base_word": "Ris",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivranac": {"meanings":["empty"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Ranac"], "compound_rule": "prefix + prefix + base","base_word": "Ranac",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivjahu": {"meanings":["deform"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Jahu"], "compound_rule": "prefix + prefix + base","base_word": "Jahu",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivukul": {"meanings":["expose","unshell"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Ukul"], "compound_rule": "prefix + prefix + base","base_word": "Ukul",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivvome": {"meanings":["disrupt","disorder"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-","Vome"], "compound_rule": "prefix + prefix + base","base_word": "Vome",  "is_generated": False,"plural_form":"", "notes":""},
"Kaivtarat": {"meanings":["dethrone","depose"],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-",], "compound_rule": "prefix + prefix + base","base_word": "",  "is_generated": False,"plural_form":"", "notes":""},

























}
#Dictionary lenght
#print(len(known_words.keys()))

#Sort words alphabethicly
known_words_dictionary = {k: known_words[k] for k in sorted(known_words)}

with open("known_words.json",'w') as kw:
    json.dump(known_words_dictionary,kw)
    kw.close()

#Dictionary item template
#{"meanings":[""],"certainty_of_translation":"high","source_of_translation":"user defined","part_of_speech_tags": ["verb"],"default_part_of_speech": "verb","is_compound": True, "compound_components": ["Ka-","Iv-",], "compound_rule": "prefix + prefix + base","base_word": "",  "is_generated": False,"plural_form":"", "notes":""},

#Suffixes
suffixes = {
"suffixes_productive":{
    "-hu": {"meanings": ["of-many","plentiful"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""},
  "-a": {"meanings": ["plural noun suffix"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":"Extracted from Voca - as game description describes Voca as 'voices/screams' , I deducted that Voc would be singular 'voice/scream'. Additionaly, it gave me an idea for plural noun suffix (-a), which I will use until I find more suitable replacement "},
    
},    

"suffixes_speculative":{
    "-un": {"meanings": ["diminutive (?)"],"certainty_of_translation":"medium","source_of_translation":"wiki_official",  "attaches_to": ["noun", "adjective"], "notes":"Contexts of '-un' known usage makes 'dimuitive(?)' meaning low probable "}
},
"suffixes_unknown":{
   "-tra": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},
    "-li": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},
    "-ia": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},  
}
}
with open("suffixes.json",'w') as suff:
    json.dump(suffixes,suff)
    suff.close()

#Prefixes
prefixes = {
"prefixes_productive" :{
  "Iv-": {"meanings": ["causative marker"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""}, 
  "Ka-": {"meanings": ["inversion/'un-(X)'"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""},
  "Sho-": {"meanings": ["Intensifier / 'Greater'"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""},
  "Uu-": {"meanings": ["Eternal-(X)"],"certainty_of_translation":"high","source_of_translation":"wiki_official", "attaches_to": ["noun"], "notes":""},
},    

"prefixes_unknown": {
    "V-": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},
    "Va-": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning"},
    "Ko-(?)": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown",  "attaches_to": ["noun"], "notes":"Lacks meaning, not confirmed if it even is a prefix"}
}     
}
with open("prefixes.json",'w') as pref:
    json.dump(prefixes,pref)
    pref.close()

#Conjunctions
conjunctions = {
"conjunctions_productive":{
    "Ra": {"meanings": ["from","out-of"],"certainty_of_translation":"medium","source_of_translation":"wiki_official", "type": "preposition", "structure": "X Ra Y", "notes":"No examples of use"},
    "Khra": {"meanings": ["the time has come for X"],"certainty_of_translation":"medium","source_of_translation":"wiki_official", "type": "temporal_conjunction","structure": "Khra X", "notes":"No examples of use"}
},
"conjunctions_unknown":{
 "Kah": {"meanings": ["?"],"certainty_of_translation":"none","source_of_translation":"wiki_unknown", "type": "conjunction", "structure": "X Kah Y", "notes":"Lacks meaning"}   
}
 }
with open("conjunctions.json",'w') as con:
    json.dump(conjunctions,con)
    con.close()

#Pronouns
pronouns = {
"pronouns_known":{
    "Veh": {"meanings": ["I am"],"type": "1st person copula","certainty_of_translation":"high","source_of_translation":"wiki_official", "grammatical_role": "subject","notes":""},
    "Re-un": {"meanings": ["us","we"],"type": "1st person plural","certainty_of_translation":"high","source_of_translation":"wiki_official", "grammatical_role": "subject","notes":""}
}
}
with open("pronouns.json",'w') as pron:
    json.dump(pronouns,pron)
    pron.close()

#Key-based translation prototype
# def translate(words):
#     words_list = words.split()
#     words_list = [w.capitalize() for w in words_list]
#     translations = []
#     for w in words_list:
#         translation = (known_words[w]["meanings"][0])
#         translations.append(translation)
#     translations = " ".join(translations)
#     return translations

# st.set_page_config(page_title="Voidtongue translator - alfa version",layout = "centered")
# st.title("Voidtongue translator - alfa version")
# st.text_input("Text",key="question_input")
# if st.button("Translate"):
#     if len(st.session_state["question_input"])>3:
#         result = translate(st.session_state["question_input"])
#         st.write("Translation:")
#         st.write(result)
#     else:
#         st.write("Too short input")