# JENOVA.py
# arendsje@g.cofc.edu
# Final Project
# Due 5/01/2017
# Designed to play "J-E-N-O-V-A" from Final Fantasy 7
# https://www.youtube.com/watch?v=J6GrZYE2il0
# Input: LPK25 Midi Keyboard and OSC via cellphone
# Output: Played via computer's midi synthesizer

from music import *
from midi import *
from osc import*

score = Score("J-E-N-O-V-A", 178) # 178 bmp

ocarinaPart = Part(79,1)
bassPart = Part(33,2)
bass2Part = Part(2,3)
stringsPart = Part(48, 4)
drumPart = Part(0,9)

### OSC Setup ### 

i = OscIn(58123)


def keyboardVolume(message):
   args = list(message.getArguments())
   Play.setVolume(message,0)

def ocarinaVolume(message):
   args = list(message.getArguments())
   Play.setVolume(message,1)

def ocarinaMute(message):
   args = list(message.getArguments())
   if args == 1:
      Play.setVolume(0,1)
   if args == 0: 
      Play.setVolume(127,1)

def bassVolume(message):
   args = list(message.getArguments())
   Play.setVolume(message,2)

def bassMute(message):
   args = list(message.getArguments())
   if args == 1:
      Play.setVolume(0,2)
   if args == 0:
      Play.setVolume(127,2)
   
def stringsVolume(message):
   args = list(message.getArguments())
   Play.setVolume(message,4)

def stringsMute(message):
   args = list(message.getArguments())
   if args == 1:
      Play.setVolume(0,4)
   if args == 0:
      Play.setVolume(127,4)

def drumsVolume(message):
   args = list(message.getArguments())
   Play.setVolume(args,9)

def drumsMute(message):
   args = list(message.getArguments())
   if args == 1:
      Play.setVolume(0,9)
   if args == 0:
      Play.setVolume(127,9)

i.onInput("/1/fader1", keyboardVolume)
i.onInput("/1/fader2", ocarinaVolume)
i.onInput("/1/fader3", bassVolume)
i.onInput("/1/fader4", stringsVolume)
i.onInput("/1/fader5", drumsVolume)
i.onInput("/1/toggle1", ocarinaMute)
i.onInput("/1/toggle2", bassMute)
i.onInput("/1/toggle3", stringsMute)
i.onInput("/1/toggle4", drumsMute)


### Midi Setup ###

m = MidiIn("Unknown vendor LPK25")
Play.setInstrument(81,0)
   
def changeInstrument(eventType, channel, pitch, dynamic):
   if dynamic == 127:
      if Play.getInstrument(0) == 81:
         Play.setInstrument(TRUMPET,0)
      else:
         Play.setInstrument(81,0)
      
def playNote(eventType, channel, pitch, dynamic):
   Play.noteOn(pitch)
   
def stopNote(eventType, channel, pitch, dynamic):
   Play.noteOff(pitch)
   
m.onNoteOn(playNote)
m.onNoteOff(stopNote)
m.onInput(176, changeInstrument)

### ocarina ###

ocarinaPhrase1 = Phrase()

ocarinaPitches1 = [AS6, A6, F6, D6, AS5, A5, F5, D5]
ocarinaDurations = [EN]*8

ocarinaPhrase2 = Phrase()
ocarinaPitches2 = [GS6, F6, CS6, C6, GS5, F5, CS5, C5]

ocarinaPhrase3 = Phrase(208)
ocarinaPitches3 = [GS6,G6,E6,C6,GS5,G5,E5,C5]

ocarinaPhrase4 = Phrase()

ocarinaPhrase1.addNoteList(ocarinaPitches1*20, ocarinaDurations*20)
ocarinaPhrase2.addNoteList(ocarinaPitches2*8, ocarinaDurations*8)
ocarinaPhrase3.addNoteList(ocarinaPitches3*4, ocarinaDurations*4)
ocarinaPhrase4.addNoteList(ocarinaPitches1*8, ocarinaDurations*8)

ocarinaPart.addPhraseList([ocarinaPhrase1, ocarinaPhrase2, ocarinaPhrase3, 
                        ocarinaPhrase4, ocarinaPhrase2, ocarinaPhrase3])

### Bass ###

bassDurations = [EN]*16

bassPhrase1 = Phrase(16)
bassPitches1 = [D3, F3, D3, F3, AS3, A3, F3, D3, 
                F3, A3, AS3, A3, F3, D3, AS2, A2]
bassPhrase2 = Phrase()
bassPitches2 = [F3, GS3, F3, GS3 ,CS4, C4, GS3, F3, 
                GS3, C4, CS4,C4, GS3, F3, CS3, C3]
                
bassPitches2a = [A2, C3, A2, C3, F3, E3, C3, A2,
                 C3, E3, F3, E3, C3, A2, F2, E2]
                 
bassPitches2b = [E3, G3, E3, G3, C4, B3, G3, E3,
                 G3, B3, C4, B3, G3, A3, C3, B2]
                 
bassPitches2c = [G3, AS3, G3, AS3, DS4, D4, AS3, G3, 
                 AS3, D4, DS4, D4, AS3, G3, DS3, D3]
                 
bassPitches2d = [C3, E3, C3, E3, GS3, G3, E3, C3, 
                 E3, G3, GS3, G3, E3, C3, GS2, G2]

bassPhrase3 = Phrase()
bassPitches3 = [F3]*16
bassPitches3a = [C3,E3,C3,E3,GS3,G3,E3,C3,
                 E3,G3,GS3,G3,E3,C3,GS2,G2]


bass2Phrase = Phrase(176)
bass2Phrase2 = Phrase(352)
bass2Pitches = [REST,F3]*5+[REST]
bass2Durations = [QN,EN]*4+[QN]+[SN]+[EN]

bassPhrase4 = Phrase()


bassPhrase1.addNoteList(bassPitches1*8, bassDurations*8)
bassPhrase1.addNoteList(bassPitches2*2, bassDurations*2)
bassPhrase2.addNoteList(bassPitches2a*2, bassDurations*2)
bassPhrase2.addNoteList(bassPitches2b*2, bassDurations*2)
bassPhrase2.addNoteList(bassPitches2c*2, bassDurations*2)
bassPhrase2.addNoteList(bassPitches2d*2, bassDurations*2)
bassPhrase2.addNoteList(bassPitches1*2, bassDurations*2)
bassPhrase3.addNoteList(bassPitches3*4, bassDurations*4)
bassPhrase3.addNoteList(bassPitches3a*2, bassDurations*2)
bassPhrase4.addNoteList(bassPitches1*4, bassDurations*4)
bassPhrase4.addNoteList(bassPitches2*2, bassDurations*2)

bass2Phrase.addNoteList(bass2Pitches*4,bass2Durations*4)
bass2Phrase2.addNoteList(bass2Pitches*4,bass2Durations*4)

bassPart.addPhraseList([bassPhrase1, bassPhrase2, bassPhrase3,
                       bassPhrase4, bassPhrase2, bassPhrase3])
                       
bass2Part.addPhraseList([bass2Phrase, bass2Phrase2])
bass2Part.setDynamic(50)

### Strings ###

s1 = [D6,F6]
s2 = [C6,E6]
s3 = [AS5,D6]
s4 = [A5,C6]
s5 = [F6,A6]
s6 = [E6,G6]
s7 = [D6,F6]
s8 = [C6,E6]

stringsPhrase1 = Phrase(16)
stringsPitches1 = [[AS4,E5,GS5],REST,REST,REST,REST,
                  [AS4,E5,GS5],D6,REST,REST,REST,REST]
                  
stringsDurations1 = ([WN*2]+[QN]+[HN+QN]+[QN]+[HN+QN]+
                     [WN]+[WN]+[QN]+[HN+QN]+[QN]+[HN+QN])

stringsPhrase2 = Phrase()
stringsPitches2 = [s1,s2,s1,s2,s3,s4,s3,s4]
stringsDurations2 = [EN]*8
stringsPitches2a = [s1,s2,s1,s2,s5,s6,s5,s6,
                    s7,s8,s7,s8,s3,s4,s3,s4]
stringsDurations2a = [EN]*16

s9 = [GS5,C6]
s10 = [G5,AS5]
s11 = [FS5,A5]
s12 = [DS5,G5]
s13 = [GS5,C6]
s14 = [G5,AS5]

stringsPhrase3 = Phrase()
stringsPitches3 = [s9,s10,s9,s10,s11,s12,s11,s12]
stringsDurations3 = [EN]*8
stringsPitches3a = [s13,s14,s13,s14,s11,s12,s11,s12]
stringsDurations3a = [EN]*8
stringsPitches3b = [[C6,DS6],[AS5,D6],[C6,DS6],
                    [AS5,D6],s13,s14,s13,s14]
stringsDurations3b = [EN]*8

stringsPitches3c = [[C6,DS6],[AS5,D6],[C6,DS6],[DS6,G6],[D6,F6],
                    [DS6,G6],[G6,AS6],[F6,GS6],[G6,AS6],[DS6,G6],
                    [D6,F6],[DS6,G6],[C6,DS6],[AS5,D6],[C6,DS6],[AS5,D6]]
                    
stringsDurations3c = [EN]*16

stringsPhrase4 = Phrase()
stringsPitches4 = [REST,REST,REST,REST,[A3,A5],[CS4,B5],[D4,C6],
                  [D4,D6],[FS4,E6],REST,REST,REST,REST,[FS3,E5],
                  [GS3,FS5],[A3,G5],[A3,A5],[CS4,B5]]
                  
stringsDurations4 = ([EN]+[HN+QN]+[EN]+[HN+QN]+[SN]*4+[WN*2]+
                     [EN]+[HN+QN]+[EN]+[HN+QN]+[SN]*4+[WN*2])
                     
stringsPitches4a = [REST,REST,[A3,G5],[A3,A5],[C4,AS5],[D4,C6],[D4,D6],
                    REST,REST,[E3,D5],[FS4,E5],[G3,F5],[A3,G5],[A3,A5]]
                    
stringsDurations4a = ([WN]+[HN+QN]+[SN]*4+[WN*2]+
                      [WN]+[HN+EN]+[SN]*4+[WN*2])

stringsPitches4b = [[C5,F5,A5],[E5,A5,C6],[D5,G5,B5],[F5,B5,D6],
                    [DS5,GS5,C6],[G5,C6,DS6],[F5,AS5,D6],[AS5,D6,F6]]
                    
stringsDurations4b = [WN]*8

stringsPitches4c = ((s8,s3)*2 + (s9,s14)*2)*4
stringsDurations4c = [EN]*32

stringsPhrase1.addNoteList(stringsPitches1, stringsDurations1)
stringsPhrase2.addNoteList(stringsPitches2*6, stringsDurations2*6)
stringsPhrase2.addNoteList(stringsPitches2a, stringsDurations2a)
stringsPhrase3.addNoteList(stringsPitches3, stringsDurations3)
stringsPhrase3.addNoteList(stringsPitches3a*3, stringsDurations3a*3)
stringsPhrase3.addNoteList(stringsPitches3b*2, stringsDurations3b*2)
stringsPhrase3.addNoteList(stringsPitches3c, stringsDurations3c)
stringsPhrase4.addNoteList(stringsPitches4, stringsDurations4)
stringsPhrase4.addNoteList(stringsPitches4a, stringsDurations4a)
stringsPhrase4.addNoteList(stringsPitches4b, stringsDurations4b)
stringsPhrase4.addNoteList(stringsPitches4c, stringsDurations4c)

stringsPart.addPhraseList([stringsPhrase1, stringsPhrase2, stringsPhrase3, 
                           stringsPhrase4, stringsPhrase1, stringsPhrase2, 
                           stringsPhrase3, stringsPhrase4])
stringsPart.setDynamic(35)

### Drums ###

d0 = [36,44,43]
d1 = [36,44,40]
d2 = [36,44]
d3= [44,40]
d4 = [36,44,47]
d5 = [44,47]
d6 = [36,44,45]
d7= [44,45]

drumPhrase1 = Phrase()
drumPhrase2 = Phrase()
drumPhrase3 = Phrase()
drumPhrase4 = Phrase()

drumPitches1 = [d2, 44, 44, d2, 44, 44,
                d2, 44, 44, d2, 44, 44]
                
drumDurations1 = ([EN]+[SN]*2)*4

drumPitches2 = [d1,40,d3,d3,d1,44,44,d2,44,44,d4,d7,44,
                d2,d7,44,d0,44,44,d6,44,44,d0,44,44]
                
drumDurations2 = [SN]*4 + ([EN]+[SN]*2)*7 

drumPitches3 = [d1,40,d3,d3,d1,44,44,d2,d3,d3,d1,40,d3,44,
                d2,d3,d3,d1,40,d3,44,d1,40,d3,d3,d1,44,44]
                
drumDurations3 = [SN]*4 + ([EN]+[SN]*2)*2 + [SN]*4 + [EN] + [SN]*2 + [SN]*8 + [EN] + [SN]*2 

drumPitches4 = [d1, 40, d3,44,d2,d3,d3,d1,44,44,d2,44,44,
                d2,d3,d3,d1,40,d3,44,d1,40,d3,d3,d1,44,44,
                d2,d5,44,d4,d5,44,d4,d5,44,d4,REST,d5,44,d5,
                44,44,d6,REST,44,44,d4,REST,44,44,d6,44,44]
                
drumDurations4 = ([SN]*4 + ([EN]+[SN]*2)*4 + [SN]*8 + ([EN]+[SN]*2)*4
                  + [SN]*4 + [EN] + [SN]*10 + [EN]+[SN]*2)

drumPitches5 = (drumPitches1 + [d2,44,44,d2,44,44,d2,44,44,d1,40,d3,d3]
                +[d1,44,44,d2,44,44,d2,44,44,d2,44,44])
                
drumDurations5 = drumDurations1 + ([EN]+[SN]*2)*3 + [SN]*4 + ([EN]+[SN]*2)*4

drumPitches6 = ([d4,44,44,d2,44,44,d6,44,44,d2,44,44,d0,
                 44,44,d2,44,44,d2,44,44,d2,44,44]+[d2,44,
                 44,d2,44,44,d2,44,44,d1,40,d3,d3])
                 
drumDurations6 = ([EN]+[SN]*2)*11 + [SN]*4

drumPitches7 = [d1,44,44,d2,44,44,d2,44,44,d2,44,44]+[d6,d7,44]*4
drumDurations7 = ([EN]+[SN]*2)*8

drumPitches8 = ([[36,44,57],46,d2,44,d2,44,d2,46]+[d2,44,d2,
                 44,d2,46,d2,44] + [d2,46,d2,44,d2,44,d2,46]
                 + [d2,44,d2,44,d2,46,d0,43,[44,43],43])
                 
drumDurations8 = [EN]*30 + [SN]*4

drumPitches9 = [[36,44,43,57],44,44,d2,
                44,44,d2,44,44,d2,44,44]


drumPhrase1.addNoteList(drumPitches1*6, drumDurations1*6)
drumPhrase1.addNoteList(drumPitches2, drumDurations2)
drumPhrase1.addNoteList(drumPitches1*2, drumDurations1*2)
drumPhrase1.addNoteList(drumPitches3, drumDurations3)

drumPhrase2.addNoteList(drumPitches1*4, drumDurations1*4)
drumPhrase2.addNoteList(drumPitches4, drumDurations4)
drumPhrase2.addNoteList(drumPitches1*4, drumDurations1*4)
drumPhrase2.addNoteList(drumPitches4, drumDurations4)

drumPhrase3.addNoteList(drumPitches5, drumDurations5)
drumPhrase3.addNoteList(drumPitches6, drumDurations6)
drumPhrase3.addNoteList(drumPitches7, drumDurations7)
drumPhrase4.addNoteList(drumPitches8*2, drumDurations8*2)
drumPhrase4.addNoteList(drumPitches9, drumDurations1)
drumPhrase4.addNoteList(drumPitches1*3, drumDurations1*3)

Mod.repeat(drumPhrase3,2)

drumPart.addPhraseList([drumPhrase1, drumPhrase2, drumPhrase3,
                        drumPhrase4, drumPhrase2, drumPhrase3, drumPhrase4])

score.addPartList([ocarinaPart, bassPart, bass2Part, stringsPart, drumPart])
Play.midi(score)