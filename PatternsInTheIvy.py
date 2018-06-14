# PatternsInTheIvy.py
# Justin Arends
# Plays part of "Patterns in the Ivy" by Opeth
 
from music import *        

score = Score("Opeth, Patterns in the Ivy", 130) # 130 bmp

guitarPart = Part(46)

guitarPhrase1 = Phrase()

pitches1 = [A2, E3, A3, B3, D4, B3, A3] 
chord1 = [A3, E3]
pitches2 = [C4, D4, B3, C4, C3, B2, A2, G2]
durations1 = [EN, EN, EN, EN, EN, EN, EN]
durations2 = [EN, EN, EN, EN, EN, EN, EN, EN]

guitarPhrase1.addNoteList(pitches1, durations1)
guitarPhrase1.addChord(chord1, EN)
guitarPhrase1.addNoteList(pitches2, durations2)
Mod.repeat(guitarPhrase1, 4)

guitarPhrase2 = Phrase()

pitches3 = [F2, C3, F3, A3, B3, A3, FS3, C3]
durations3 = [EN, EN, EN, EN, EN, EN, EN, EN]
pitches4 = [FS2, CS3, B3, AS3, FS3, C3, FS3, A3]
durations4 = [EN, EN, EN, EN, EN, EN, EN, EN]
pitches5 = [G2, D3, A3, BF3, D4, B3, A3, A2]
durations5 = [EN, EN, EN, EN, EN, EN, EN, EN]
pitches6 = [AF2, C3, E3, A3, B3, C4, B3, G3]
durations6 = [EN, EN, EN, EN, EN, EN, EN, EN]

guitarPhrase2.addNoteList(pitches3, durations3)
guitarPhrase2.addNoteList(pitches4, durations4)
guitarPhrase2.addNoteList(pitches5, durations5)
guitarPhrase2.addNoteList(pitches6, durations6)

guitarPart.addPhrase(guitarPhrase1)
guitarPart.addPhrase(guitarPhrase2)

score.addPart(guitarPart)
Mod.repeat(score, 2)

Play.midi(score)
