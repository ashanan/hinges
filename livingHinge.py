import svgcuts
import math

#consants based on http://www.thingiverse.com/thing:15845
#units = mm

kerf = .08
gap = 1.85
cut_distance = 1.5
cut_length = 13.3
offset_cut_length = cut_length / 2
hinge_height = 90
hinge_width = 110

layer = svgcuts.Layer(hinge_width, hinge_height)

cut_columns = int(math.floor(hinge_width / (kerf + cut_distance)))
cut_rows = int(math.floor(hinge_height / (cut_length + gap)))

#[ svgcuts.Point(n*(kerf + cut_distance), (n+1)*kerf + n*cut_distance) for n in range(0,cut_columns)]
# [ svgcuts.Line(svgcuts.Point(n*(kerf + cut_distance),0), svgcuts.Point((n+1)*kerf + n*cut_distance),0) for n in range(0,cut_columns)]
# [layer.add_line(svgcuts.Line(svgcuts.Point(n*(kerf + cut_distance), 0),svgcuts.Point((n+1)*kerf + n*cut_distance,0))) for n in range(0,cut_columns)]

for x in range(0, cut_columns):
    for y in range(0, cut_rows):
        if cut_length == offset_cut_length:
            cut_length *= 2

        if x % 2 == 0:
            offset = 0
        elif y != 0:
            offset = -offset_cut_length

        if (y == 0 or y == cut_rows) and x % 2 == 1:
            cut_length = offset_cut_length

        upperLeftPoint = svgcuts.Point(x * (kerf + cut_distance), y * (cut_length + gap) + offset)
        upperRightPoint = svgcuts.Point((x+1)*kerf + x*cut_distance, y * (cut_length + gap) + offset)

        lowerLeftPoint = svgcuts.Point(x * (kerf + cut_distance), (y + 1) * cut_length + y * gap + offset)
        lowerRightPoint = svgcuts.Point((x + 1)*kerf + x*cut_distance, (y + 1) * cut_length + y * gap + offset)

        layer.add_line(svgcuts.Line(upperLeftPoint, upperRightPoint))
        layer.add_line(svgcuts.Line(upperRightPoint, lowerRightPoint))
        layer.add_line(svgcuts.Line(lowerRightPoint, lowerLeftPoint))
        layer.add_line(svgcuts.Line(lowerLeftPoint, upperLeftPoint))
    else:
        if x % 2 == 1:
            y += 1
            upperLeftPoint = svgcuts.Point(x * (kerf + cut_distance), y * (cut_length + gap) + offset)
            upperRightPoint = svgcuts.Point((x+1)*kerf + x*cut_distance, y * (cut_length + gap) + offset)

            lowerLeftPoint = svgcuts.Point(x * (kerf + cut_distance), (y + 1) * cut_length + (y-1) * gap + offset - offset_cut_length)
            lowerRightPoint = svgcuts.Point((x + 1)*kerf + x*cut_distance, (y + 1) * cut_length + (y-1) * gap + offset - offset_cut_length)

            layer.add_line(svgcuts.Line(upperLeftPoint, upperRightPoint))
            layer.add_line(svgcuts.Line(upperRightPoint, lowerRightPoint))
            layer.add_line(svgcuts.Line(lowerRightPoint, lowerLeftPoint))
            layer.add_line(svgcuts.Line(lowerLeftPoint, upperLeftPoint))

layer.write("test.svg")
