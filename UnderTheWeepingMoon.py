# UnderTheWeepingMoon.py
# Justin Arends
# arendsje@g.cofc.edu
# Homework 2
# Due 2/06/2017
# Plays part of "Under The Weeping Moon" by Opeth
# Input: None.
# Output: Played via computer's synthesizer.
 
from music import *        

score = Score("Opeth, Under The Weeping Moon", 120) # 120 bmp

guitarPart = Part(46, 0) # Acoustic Rhythm
guitarPart2 = Part(26, 1) # Acoustic Lead
electricPart = Part(29, 2) # Electric Rhythm
electricPart2 = Part(40, 3) # Electric Lead
bassPart = Part(33, 4)
drumPart = Part(0,9)

##### Acoustic Rhythm ########

guitarPhrase1 = Phrase()

pitches1 = [AS3] 
chord1 = [E3,B3,E4,G4,B4,E5]
pitches2 = [D4, E4, D4, AS3, E3, AS3, AS3]*3
durations1 = [EN+(HN*1.5)+HN+EN]
durations2 = [EN, EN, EN, EN, (QN*1.5), EN, WN]*3
pitches3 = [D4, E4, D4, AS3, A4, G4, A4, AS4, C5, A4, G4, G4, 
F4, F4, E4, E4, B3, E3, G3, B3, A3, A4, E4, E4, D4, C4, B3]
durations3 = [EN, EN, EN, EN, EN, SN, SN, EN, EN, (QN*1.5), EN, EN, EN, 
EN, EN, EN, EN, EN, EN, (QN*1.5), EN, (QN*1.5), EN, EN, EN, EN, EN]

guitarPhrase1.addChord(chord1, HN)
guitarPhrase1.addNoteList(pitches1, durations1)
guitarPhrase1.addNoteList(pitches2, durations2)
guitarPhrase1.addNoteList(pitches3, durations3)

######### End Acoustic Rhythm #########


######## Acoustic Lead ###########

guitarPhrase2 = Phrase(10.0)

chord2_1 = [E4, B4, E5, G5, B5]
pitches2_1 = [C5, B4, C5, B4, A4, B4, A4, G4, A4, E4, A4, A4, G4, G4, F4, F4,
E4, E4, G4, E4, D4, E4, D4, D4]
durations2_1 = [EN, SN, SN, SN, EN, EN, EN, EN, EN,
(QN*1.5), EN, (QN*1.5), EN, EN, EN, EN, EN, EN, EN, EN, EN, (QN*1.5), EN, HN+EN]
pitches2_2 = [C5, B4, C5, B4, A4, B4, A4, G4, A4, E4, A4, A4, A4, A4, G4, G4, F4]
durations2_2 = [EN, SN, SN, SN, EN, EN, EN, EN, EN,
(QN*1.5), EN, (QN*1.5), EN, EN, EN, EN, EN]

guitarPhrase2.addChord(chord2_1, WN*3)
guitarPhrase2.addNoteList(pitches2_1, durations2_1)
guitarPhrase2.addNoteList(pitches2_2, durations2_2)

######## End Acoustic Lead ########

######### Bass ################

bassPhrase1 = Phrase(50)
bassPhrase1.setTempo(125)

pitchesB_1 = [E2, E2, E2, REST, E2, E2]
durationsB_1 = [EN, EN, EN, (QN*1.5), EN, EN]
pitchesB_2 = [E2, G2, AS2, D3, E3, D3, B2]*7
durationsB_2 = [(QN*1.5), EN, WN, EN, EN, EN, EN]*7
pitchesB_3 = [E2, G2, AS2]
durationsB_3 = [(QN*1.5), EN, WN]

bassPhrase1.addNoteList(pitchesB_1, durationsB_1)
bassPhrase1.addNoteList(pitchesB_2, durationsB_2)
bassPhrase1.addNoteList(pitchesB_3, durationsB_3)

######## End Bass ##############

######## Electric Rhythm #######

electricPhrase1 = Phrase(50)
electricPhrase1.setTempo(125)
electricPhrase2 = Phrase(54)
electricPhrase2.setTempo(125)

pitchesE_1 = [G3, AS3, D4, E4, D4, A3]
durationsE_1 = [EN, WN, EN, EN, EN, EN]
pitchesE_2 = [A4, G4, A4, AS4, C5, G4, A4, G4, F4, F4, E4, E4, D4, E3, G3,
B3, A3, E4, D4, D4, C4, C4, B3, B3, C4, B3]
durationsE_2 = [EN, SN, SN, EN, EN, (QN*1.5), EN, EN, EN, EN, EN, EN,
EN, EN, EN, (QN*1.5), EN, (QN*1.5), EN, EN, EN, EN, EN, EN, EN, QN]


electricPhrase1.addChord([E3, B3, E4], EN)
electricPhrase1.addChord([E3, B3, E4], EN)
electricPhrase1.addChord([E3, B3, E4], EN)
electricPhrase1.addNote(REST, QN*1.5)
electricPhrase1.addChord([E3, B3, E4], EN)
electricPhrase1.addChord([E3, B3, E4], EN)
electricPhrase2.addChord([E3, B3, E4], QN*1.5)
electricPhrase2.addNoteList(pitchesE_1, durationsE_1)
Mod.repeat(electricPhrase2, 2)
electricPhrase2.addNoteList(pitchesE_2, durationsE_2)
Mod.repeat(electricPhrase2, 2)

######### End Electric Rhythm ########

######## Electric Lead ##########

electricPhrase3 = Phrase(50)
electricPhrase3.setTempo(125)
electricPhrase4 = Phrase(54)
electricPhrase4.setTempo(125)

pitchesE_3 = [E4, D4, D4, C5, B4, C5, B4, A4, B4, A4, G4, A4,
E4, A4, A4, G4, G4, F4, F4, E4, E4, G4, E4]
durationsE_3 = [(QN*1.5), EN, HN+EN, EN, SN, SN, SN, EN, EN, EN,
EN, EN, (QN*1.5), EN, (QN*1.5), EN, EN, EN, EN, EN, EN, EN, QN*.75]

electricPhrase3.addChord([E3, B3, E4], EN)
electricPhrase3.addChord([E3, B3, E4], EN)
electricPhrase3.addChord([E3, B3, E4], EN)
electricPhrase3.addNote(REST, QN*1.5)
electricPhrase3.addChord([E3, B3, E4], EN)
electricPhrase3.addChord([E3, B3, E4], EN)
electricPhrase4.addNoteList(pitchesE_3, durationsE_3)
Mod.repeat(electricPhrase4, 4)

guitarPart.addPhrase(guitarPhrase1)
guitarPart2.addPhrase(guitarPhrase2)
bassPart.addPhrase(bassPhrase1)
electricPart.addPhrase(electricPhrase1)
electricPart.addPhrase(electricPhrase2)
electricPart2.addPhrase(electricPhrase3)
electricPart2.addPhrase(electricPhrase4)

####### End Electric Lead #########

########### Drums ################

drumPhrase = Phrase(50)
drumPhrase.setTempo(125)
drumPhrase2 = Phrase(54)
drumPhrase2.setTempo(125)
drumPhrase3 = Phrase(70)
drumPhrase3.setTempo(125)
drumPhrase4 = Phrase(78)
drumPhrase4.setTempo(125)


drumPhrase.addChord([36, 51], EN)
drumPhrase.addChord([36, 51], EN)
drumPhrase.addChord([36, 51], EN)
drumPhrase.addNote(REST, QN*1.5)
drumPhrase.addChord([36, 51], EN)
drumPhrase.addChord([36, 51], EN)
drumPhrase2.addChord([36, 51], QN)
drumPhrase2.addNoteList([46, 36], [EN]*2)
drumPhrase2.addChord([48, 50], QN)
drumPhrase2.addNoteList([46, 36], [EN]*2)
drumPhrase2.addChord([36, 46], QN)
drumPhrase2.addNoteList([46, 36], [EN]*2)
drumPhrase2.addChord([48, 50], QN)
drumPhrase2.addNoteList([46, 36], [EN]*2)
Mod.repeat(drumPhrase2, 2)
drumPhrase3.addChord([36, 46], EN)
drumPhrase3.addNote(48, EN)
drumPhrase3.addChord([48,46],EN)
drumPhrase3.addNote(36, EN)
drumPhrase3.addChord([48, 51], QN)
drumPhrase3.addNoteList([46, 36], [EN, EN])
drumPhrase3.addChord([46, 36], QN)
drumPhrase3.addNoteList([46, 48, 46, 36], [EN]*4)
drumPhrase3.addChord([36, 46], QN)
drumPhrase4.addNoteList([46, 36], [EN]*2)
drumPhrase4.addNoteList([46, 36], [EN]*2)
drumPhrase4.addChord([48, 50], QN)
drumPhrase4.addChord([48, 50], QN)
drumPhrase4.addChord([47, 55], QN)
drumPhrase4.addChord([45, 53], QN)
Mod.repeat(drumPhrase2, 2)
Mod.repeat(drumPhrase3)
Mod.repeat(drumPhrase2)

drumPart.addPhrase(drumPhrase)
drumPart.addPhrase(drumPhrase2)
drumPart.addPhrase(drumPhrase3)
drumPart.addPhrase(drumPhrase4)

######## End Drums ###########


score.addPart(guitarPart)
score.addPart(guitarPart2)
score.addPart(bassPart)
score.addPart(electricPart)
score.addPart(electricPart2)
score.addPart(drumPart)

Play.midi(score)
