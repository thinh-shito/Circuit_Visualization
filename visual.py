import streamlit as st
import process

def app():
	relation = st.text_input(label ='Nhập vào đặc tả',)
	values = st.text_input(label = 'Nhập vào giá trị các điện trở',)
	run = st.button(label='Biểu diễn',)
	if run:
		result = process.main(relation, values)
		st.image('main.jpg',caption = 'Sơ đồ mạch điện')
		# st.write('dddđ',process.grid(grid(relation)))
		st.write('Tổng trở của mạch điện = ', result)
if __name__ == '__main__':
	
	app()

	pass