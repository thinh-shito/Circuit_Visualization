
import schemdraw 
import schemdraw.elements as elm


def draw(root, C):
	with schemdraw.Drawing(show = False) as d:
		if C[root]['child'] == []:
				d += elm.ResistorIEC().label(root)
		else:	
			child_list = C[root]['child']
			if C[root]['relation'] == 'nt':
				l = 0.0
				for i in range(len( child_list) - 1 ):
					l += C[child_list[i]]['length']
					d += elm.ElementDrawing(draw(child_list[i],C))
					if C[child_list[i]]['relation'] == 'ss' and C[child_list[i + 1]]['relation']  == 'ss':
						d += elm.Line().length(1).at((l,0.0))
						l += 1
					# d.save(str(i)+'temp.jpg')
				d += elm.ElementDrawing(draw(child_list[-1],C))
			else: 
				l = C[root]['length']
				lc, hc = C[child_list[0]]['length'], C[child_list[0]]['height']
				d.push()
				# print(lc, hc, l)
				if lc < l:
						d+= elm.Line().length((l - lc) / 2)
						d += elm.ElementDrawing(draw(child_list[0],C))
						d+= elm.Line().length((l - lc) / 2)
				else:
					d += elm.ElementDrawing(draw(child_list[0],C))

				
				for child in child_list[1:]:
					# print(child, hc)
					d.pop()
					d += elm.Line().length(hc).down()
					d.push()
					lc = C[child]['length']
					temp = draw(child,C)
					if lc < l:
						d += elm.Line().length((l - lc) / 2).right()
						d += elm.ElementDrawing(temp).right()
						d += elm.Line().length((l - lc)/2)
					else:
						d += elm.ElementDrawing(temp).right()
					d += elm.Line().length(hc).up()
					hc = C[child]['height']
		# d.save(root+'draw.jpg')
	return d
def main(root,C):
	with schemdraw.Drawing(show = False) as d:
		d += elm.Dot().label('A')
		d += elm.Line()
		d += elm.ElementDrawing(draw(root,C))
		d += elm.Line().at((C[root]['length'] + 3,0.0))
		d += elm.Dot().label('B')
		d.save('main.jpg')

if __name__ == '__main__':
	C = 	{	
		'R1_2_3_4_5_6': 
					{	
						'relation': 'nt', 
						'value': 16.4686685136897, 
						'child': ['R1_2_3_4', 'R5_6'], 
						'length': 20, 
						'height': 6
					}, 
		'R1_2_3_4': 
					{	
						'relation': 'ss', 
						'value': 11.853283898305087, 
						'child': ['R1_2_3', 'R4'], 
						'length': 13, 
						'height': 6
					}, 
		'R1_2_3': 
					{	
						'relation': 'nt', 
						'value': 80.5, 
						'child': ['R1', 'R2', 'R3'], 
						'length': 9, 
						'height': 3
					}, 
		'R1': 
					{	
						'relation': '', 
						'value': 10.4, 
						'child': [], 
						'length': 3, 
						'height': 3
					}, 
		'R2': 
					{	
						'relation': '', 
						'value': 20.1, 
						'child': [], 
						'length': 3, 
						'height': 3
					}, 
		'R3': 
					{	
						'relation': '', 
						'value': 50, 
						'child': [], 
						'length': 3, 
						'height': 3
					}, 
		'R4': 
					{	
						'relation': '', 
						'value': 13.9, 
						'child': [], 
						'length': 3, 
						'height': 3
					}, 
		'R5_6': 
					{	
						'relation': 'ss', 
						'value': 4.615384615384615, 
						'child': ['R5', 'R6'], 
						'length': 7, 
						'height': 6
					}, 
		'R5': 
					{	
						'relation': '', 
						'value': 60, 
						'child': [], 
						'length': 3, 
						'height': 3
					}, 
		'R6': 
					{	
						'relation': '', 
						'value': 5, 
						'child': [], 
						'length': 3, 
						'height': 3
					}
	}
	node = list(C.keys())[0]
	draw('R5_6',C)