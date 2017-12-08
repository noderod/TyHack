"""
BASICS

A basic program that uses a pre-defined library to break the Enigma machine.
Writes all posible combinations to a text file.
"""
from enigma.machine import EnigmaMachine
import itertools as itt


To_Break = 'DFBQUFQLKLYIJXVNVZIPBLHKGBIIUSVUIOTIKTIYKUMARADPVLVSZIFIFEXJDKNIAEHIDVFEXEFRMR'+\
'SEDYBGQWSTVHBKOHLPLVHOIILJSYKYSJEFSEVXRVXQFBJSLDWUMWFJLCWWUHFLRQNGLQTDD'+\
'FYHEVEHMKXQUZPXDLZELMPTTWHQWIONQUXPHZURPCAIVBMMYMFJEULHDECPYNJIYPFAQATPPGIJ'+\
'TYQUJAIPFNZMCUUULMVPISEEEEUYJQUSGVWMFSOVSSEXYGJVEPDEIVFCKRYTOSLQWGESXYIDIRBVK'+\
'DCHNBOZWXMWZVBINPUEUQTWUWQOGRNDCXBXDINDWUXGCXXXJATPNGDGDTNLILEDRUKYJVBRHWCZV'+\
'KFPIXLWPHUCFREKETWMESZVJYDOCJAWRPCHAHUOFGSYYARMATTILSDSKHYAYMJJTESHWEYLULTLGD'+\
'MJWJKDRVCWKLDMLKRNNCDYAXBHEFYZRPGEWMRVMOIJPXSIXPEOCOXCPHCEMENWVJHULCFGTBAWZRSP'

# Finds all the combinations of rotors
Rot_Ava = ['I', 'II', 'III', 'IV', 'V'] # Establishes all the available rotors
# All the available ring setting, from 0 to 25 (both included)
Ring_Ava = list(range(0, 26))
# List of letters
Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']


# Obtains all the combinations for the rotors
C_Rot = list(itt.permutations(Rot_Ava, 3))

# Combines them into a string
C_Rot_str = []
for hh in C_Rot:
    Cures = ''
    for nvnv in hh:
        Cures += nvnv+' '
    C_Rot_str.append(Cures)

C_Rot = C_Rot_str
print(C_Rot)

# Finds all the permutations of the rings
P_Ring = list(itt.permutations(Ring_Ava, 3))


# Writes the result to a text file
with open('All_Enigma.txt', 'w'):




# setup machine according to specs from a daily key sheet:

machine = EnigmaMachine.from_key_sheet(
       rotors='IV II V',
       reflector='B',
       ring_settings=[25, 25, 25])

# set machine initial starting position
machine.set_display('WXC')

# decrypt the message key
msg_key = machine.process_text('KCH')

# decrypt the cipher text with the unencrypted message key
machine.set_display(msg_key)

plaintext = machine.process_text(To_Break)

print(plaintext)
