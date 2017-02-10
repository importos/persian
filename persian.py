# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import persian.bidi
import persian.persian_reshaper as pr
from persian.bidi import algorithm

class perisn_test(sublime_plugin.WindowCommand):
	def run(self):
		w = self.window
		p1=w.get_output_panel('persian_panel')
		if p1.window()==None:
			w.run_command('show_panel', { 'panel': 'output.persian_panel' })
		print (p1.id())
		print (w.panels())
		p1.run_command("insert",{"characters": '123'})
class persian_show(sublime_plugin.WindowCommand):
	def run(self,data):
		w = self.window
		p1=w.get_output_panel('persian_panel')
		if p1.window()==None:
			w.run_command('show_panel', { 'panel': 'output.persian_panel' })
		print(data)
		p1.run_command("insert",{"characters": data})
class persian_event(sublime_plugin.EventListener):
	def convert_persian(self,data):
		return algorithm.get_display(pr.reshape(data),'utf-8',True)
	def on_selection_modified(self, view):
		o1=''
		pre=''
		for itm in view.sel():
			txt=view.substr(view.line(itm))
			o1+=pre
			o1+=txt
			pre='\n'
		po1=self.convert_persian(o1)
		# print(po1)
		if view.window()!=None:
			p1=view.window().get_output_panel('persian_panel')
			# print(p1.id(),view.id())
			if p1.view_id!=view.view_id:
				# print(po1)
				view.window().run_command('persian_show',{'data':po1})
			else:
				return False

