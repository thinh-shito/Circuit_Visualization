import schemdraw
import schemdraw.elements as elm

# with schemdraw.Drawing() as d:
# with schemdraw.Drawing(show = False) as d:
# 	d += (start := elm.Dot(open = True).label('A'))
# 	d += (str_line := elm.Line())
# 	d.push()
# 	d += (str_hor_line_down := elm.Line()).down()
# 	d.pop()
# 	d += (str_hor_line := elm.Line()).up()
# 	d += (R1:= elm.ResistorIEC().label('R1').right())
# 	d += elm.ResistorIEC().label('R2')
# 	d += elm.ResistorIEC().label('R3')
# 	d += elm.Line().down() 
# 	d.push()
# 	d += elm.Line().right()
# 	d += (end := elm.Dot(open = True).label('B'))
# 	d.pop()
# 	d.push()
# 	d += (a:= elm.Line().down())
# 	# d += elm.Line().left()
# 	d += elm.ResistorIEC().label('R4').left().endpoints(a.end,str_hor_line_down.end)
# 	# d += elm.Line().left()
# 	d.pop()
# 	d.pop()

# 	d.save('schem_image.jpg')
# print(d.start, d.end)
# with schemdraw.Drawing(show = False) as d2:
# 	d2 += (r:= elm.SourceV())
# 	d2 += (l:= elm.Line())
# 	d2 += elm.ElementDrawing(d).at(r.start, l.end)
# 	d2 += elm.Line()
# 	d2 += elm.ElementDrawing(d)

# 	d2.save('a.jpg')

with schemdraw.Drawing(show = False) as d:
	# d.push()
	d += elm.ResistorIEC().label('A')
	d += elm.ResistorIEC().label('B')
	d += elm.ResistorIEC().label('C')

with schemdraw.Drawing(show = False) as d1:
	# d1.push()
	d1 += elm.ResistorIEC().label('A')

with schemdraw.Drawing(show = False) as d2:
	d2.push()
	# d2 += elm.Line().up()
	d2 += elm.ResistorIEC().label('A')
	d2.pop()
	d2 += elm.Line().down()
	d2.push()
	d2 += elm.ResistorIEC().label('B').right()
	d2.pop()
	d2 += elm.Line().down()
	d2 += elm.ResistorIEC().label('C').right()
	d2 += elm.Line().up()
	d2 += elm.Line().up()

	# d += elm.ResistorIEC().label('C')
	d2.save('test.jpg')

with schemdraw.Drawing(show = False) as d3:
	d3.push()
	d3 += elm.ElementDrawing(d)
	d3.pop()
	d3 += elm.Line().down()
	
	d3 += elm.ElementDrawing(d1).right()
	d3 += elm.ElementDrawing(d2)
	d3 += elm.Line()
	d3 += elm.Line().up()
	d3.save('test1.jpg')

with schemdraw.Drawing(show = False) as d4:
	d4 += elm.Line()
	d4 += elm.ElementDrawing(d3)
	d4 += elm.Line()
	d4.save('test2.jpg')

with schemdraw.Drawing(show = False) as d5:
	# d5.config(unit = 1)
	d5 += elm.ElementDrawing(d4)
	d5 += elm.ElementDrawing(d4)

	d5.save('test5.jpg')

	
if __name__ == '__main__':
	pass

	# DT = '[[R1+R2+R3]*R4]+[R5+R6]'
	# R = {'R5':elm.ResistorIEC(),
	# 	'R6': elm.ResistorIEC()
	# 	}
	# with schemdraw.Drawing(show = False) as d2:
	# 	d2 += R['R5']
	# 	d2 += R['R6']
	# 	d2.save('ssd.jpg')
	
	