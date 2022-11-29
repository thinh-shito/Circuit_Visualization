import re
import schemdraw
import schemdraw.elements as elm
import draw

def grid(relation):
	pattern = '([\[\]\(\),]|\w+)'
	return re.findall(pattern, relation)

def create_tree(DT,values ,pos = 0):
	dict_ = 	{
				'relation': '',
				'value' : 0.0,
				'child': [],
				'length': 0,
				'height': 0,
			}
	tree = dict()
	cnt = 'nt' if DT[pos] == '(' else 'ss'
	dict_['relation'] = cnt
	pos += 1
	sum = 0

	while pos < len(DT):
		if DT[pos] == ',': pass
		elif DT[pos] in ['(','[']:
			d, pos, c = create_tree(DT, values, pos)
			dict_['child'].append(c)
			tree.update(d.copy())
			sum += d[c]['value'] if cnt == 'nt' else 1/d[c]['value']
			del d
		elif DT[pos] in [')',']']:
			break
		else: 
			dict_['child'].append(DT[pos])
			sum += values[DT[pos]] if cnt == 'nt' else 1.0/ values[DT[pos]]
			child = 	{
						DT[pos]:	{
									'relation': '',
									'value' : values[DT[pos]],
									'child': [],
									'length': 3,
									'height': 3,
								}
					}
			tree.update(child)

		pos += 1

	if cnt == 'ss':
		sum = 1.0/sum
	dict_['value'] = sum
	
	l = 0
	h = 0
	if cnt == 'nt':

		for child in dict_['child']:
			l += tree[child]['length']
			h = max( tree[child]['height'], h)

		for i in range( len( dict_['child'] ) - 1 ):
			if tree[dict_['child'][i]]['relation'] == tree[dict_['child'][i + 1]]['relation']  == 'ss':
				l += 1
	else:
		for child in dict_['child']:
			l = max( tree[child]['length'], l)
			h += tree[child]['height']
	dict_['length'], dict_['height'] = l, h

	# print(sum)
	node = 'R' + "_".join(re.findall("\d+","".join(dict_['child'])))
	tree = dict({node: dict_}) | tree
	return tree, pos, node
def main(dt, values):
	# value[values)
	value_split = re.split('=|,',values)
	print(value_split)
	value_dict = {resistor : float(value) for resistor, value in zip(value_split[::2],value_split[1::2] )}
	# print(value_dict)
	DT = grid(dt)
	tree,_,_ = create_tree(DT, value_dict)
	node = list(tree.keys())[0]
	draw.main( list(tree.keys())[0], tree)
	
	return tree[node]['value']


if __name__ == '__main__':
	values = 'R1=10.4,R2=20.1,R3=50,R4=13.9,R5=60,R6=5,R7=80'
	# values = '[R1=5,R2=8,R3=9,R4=10,R5=7.5,R6=9]'
	# DT = ['(', '[', '(', 'R1', ',', 'R2', ',', 'R3', ')', ',', 'R4', ']', ',', '[', 'R5', ',', 'R6', ']', ')']
	DT = '([([R1,(R4,[R3,R2])],R5,R6),R2],R5,[(R3,R4),R1])'
	# DT ='[R1,([R2,R3],[R4,R5])]'
	main(DT,values)


