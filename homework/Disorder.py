# Disorder.py
# Justin Arends
# arendsje@g.cofc.edu
# Homework 4
# Due 3/27/2017
# Plays: Various wave files by Metallica, Alice in Chains, Megadeth, Tool, Dream Theater, and System of a Down.
# Input: User input on display interface.
# Output: Played via computer's synthesizer.
 
from music import *    
from gui import *    

d = Display("Disorder", 550, 400)

### Creates the AudioSamples ####

a = AudioSample("aerials.wav")
m = AudioSample("misery.wav")
w = AudioSample("would.wav")
t = AudioSample("toxicity.wav")
f = AudioSample("46&2.wav")
p = AudioSample("puppets.wav")
o = AudioSample("omen.wav")
pa = AudioSample("panic.wav")
ps = AudioSample("peacesells.wav")

### Functions for the buttons ###

def misery():
    m.loop()
    
def miseryStop():
   m.stop()
   
def would():
    w.loop()

def wouldStop():
   w.stop()

def aerials():
   a.loop()

def aerialsStop():
   a.stop()
   
def panic():
   pa.loop()

def panicStop():
   pa.stop()

def toxicity():
    t.play()
 
def fourty():
    f.play()

def omen():
   o.play()
   
def puppets():
   p.play()
   
def peacesells():
   ps.loop()

def peacesellsStop():
   ps.stop()
        
### Function for the slider ###

def peacesellsVolume(peacesellsSlider):
   ps.setVolume(peacesellsSlider)

### Creates the buttons and the slider ###

miseryButton = Button("Misery", misery)
miseryStopButton = Button("Misery Stop", miseryStop)
wouldButton = Button("Would?", would)
wouldStopButton = Button("Would Stop", wouldStop)
aerialsButton = Button("Aerials", aerials)
aerialsStopButton = Button("Aerials Stop", aerialsStop)
panicButton = Button("Panic", panic)
panicStopButton = Button("Panic Stop", panicStop)
toxicityButton = Button("Toxicity", toxicity)
fourtyButton = Button("46&2", fourty)
omenButton = Button("Omen", omen)
puppetsButton = Button("Puppets", puppets)
peaceSellsButton = Button("Peace Sells, But Who's Buyin?", peacesells)
peaceSellsStopButton = Button("Peace Sells, But No One's Buyin", peacesellsStop)
peacesellsSlider = Slider(VERTICAL, 0, 100, 0, peacesellsVolume)

### Adds the buttons and slider to the display ###

d.add(miseryButton, 160, 150)
d.add(miseryStopButton, 140, 180)
d.add(wouldButton, 245, 150)
d.add(wouldStopButton, 240, 180)
d.add(aerialsButton, 335, 150)
d.add(aerialsStopButton, 330, 180)
d.add(panicButton, 425, 150)
d.add(panicStopButton, 430, 180)
d.add(toxicityButton, 160, 210)
d.add(fourtyButton, 260, 210)
d.add(omenButton, 340, 210)
d.add(puppetsButton, 440, 210)
d.add(peaceSellsButton, 240, 250)
d.add(peaceSellsStopButton, 240, 280)
d.add(peacesellsSlider, 120, 150)