from sys import argv
import hinge

#consants based on http://www.thingiverse.com/thing:15845
#units = mm
kerf = .08
gap = 1.85
cut_distance = 1.5
cut_length = 13.3
offset_cut_length = cut_length / 2

if len(argv) > 1:
    hinge_height = int(argv[1])
    hinge_width = int(argv[2])
else:
    hinge_height = 90
    hinge_width = 110

h = hinge.Hinge(hinge_width, hinge_height, cut_distance, cut_length, kerf, gap)  

h.write("test.svg")
