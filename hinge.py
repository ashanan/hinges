import svgcuts
import math

class Hinge(object):
    def __init__(self, width, height, cut_distance, cut_length, kerf, gap):
        self.width = width
        self.height = height  
        self.cut_distance = cut_distance
        self.cut_length = cut_length
        self.kerf = kerf
        self.gap = gap
        self.offset_cut_length = cut_length / 2
        self.layer = None

    def __eq__(self, other):
        foreach

    def render(self):
        if self.layer == None:
            self.layer = svgcuts.Layer(self.width, self.height)
            self.prepare_hinge()
        return self.layer.render()

    def write(self, filename):
        if self.layer == None:
            self.layer = svgcuts.Layer(self.width, self.height)
            self.prepare_hinge()
        return self.layer.write(filename)
        
    def prepare_hinge(self):
        cut_columns = int(math.floor(self.width / (self.kerf + self.cut_distance)))
        cut_rows = int(math.floor(self.height / (self.cut_length + self.gap)))
        	
        for x in range(0, cut_columns):
            for y in range(0, cut_rows):
                if self.cut_length == self.offset_cut_length:
                    self.cut_length *= 2

                if x % 2 == 0:
                    offset = 0
                elif y != 0:
                    offset = -self.offset_cut_length

                if (y == 0 or y == cut_rows) and x % 2 == 1:
                    self.cut_length = self.offset_cut_length

                upperLeftPoint = svgcuts.Point(x * (self.kerf + self.cut_distance), y * (self.cut_length + self.gap) + offset)
                upperRightPoint = svgcuts.Point((x+1)*self.kerf + x*self.cut_distance, y * (self.cut_length + self.gap) + offset)

                lowerLeftPoint = svgcuts.Point(x * (self.kerf + self.cut_distance), (y + 1) * self.cut_length + y * self.gap + offset)
                lowerRightPoint = svgcuts.Point((x + 1)*self.kerf + x*self.cut_distance, (y + 1) * self.cut_length + y * self.gap + offset)

                self.layer.add_line(svgcuts.Line(upperLeftPoint, upperRightPoint))
                self.layer.add_line(svgcuts.Line(upperRightPoint, lowerRightPoint))
                self.layer.add_line(svgcuts.Line(lowerRightPoint, lowerLeftPoint))
                self.layer.add_line(svgcuts.Line(lowerLeftPoint, upperLeftPoint))
            else:
                if x % 2 == 1:
                    y += 1
                    upperLeftPoint = svgcuts.Point(x * (self.kerf + self.cut_distance), y * (self.cut_length + self.gap) + offset)
                    upperRightPoint = svgcuts.Point((x+1)*self.kerf + x*self.cut_distance, y * (self.cut_length + self.gap) + offset)

                    lowerLeftPoint = svgcuts.Point(x * (self.kerf + self.cut_distance), (y + 1) * self.cut_length + (y-1) * self.gap + offset - self.offset_cut_length)
                    lowerRightPoint = svgcuts.Point((x + 1)*self.kerf + x*self.cut_distance, (y + 1) * self.cut_length + (y-1) * self.gap + offset - self.offset_cut_length)

                    self.layer.add_line(svgcuts.Line(upperLeftPoint, upperRightPoint))
                    self.layer.add_line(svgcuts.Line(upperRightPoint, lowerRightPoint))
                    self.layer.add_line(svgcuts.Line(lowerRightPoint, lowerLeftPoint))
                    self.layer.add_line(svgcuts.Line(lowerLeftPoint, upperLeftPoint))
