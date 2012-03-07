import svgcuts
import math

#consants based on http://www.thingiverse.com/thing:15845
#units = mm

kerf = .08
gap = 1.85
cut_distance = 1.5
cut_length = 13.3
hinge_height = 90
hinge_width = 110

cut_columns = math.floor(hinge_width / (kerf + cut_distance))

print cut_columns
