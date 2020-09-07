from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
#Aplicativo que conta coisas em python
class Aplicativo(FloatLayout):
	def soma (self):
		self.ids.lb.text = str(int(self.ids.lb.text)+1)
	def subt(self):
		self.ids.lb.text = str(int(self.ids.lb.text)-1)
	def reset(self):
		self.ids.lb.text = str(0)


class AppContagem(App):
	pass

if __name__ == '__main__':
	AppContagem().run()
