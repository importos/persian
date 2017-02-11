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
class persian_panel_show(sublime_plugin.WindowCommand):
	def run(self):
		w = self.window
		if w.find_output_panel('persian_panel')==None:
			w.create_output_panel('persian_panel')
		w.run_command('show_panel', { 'panel': 'output.persian_panel' })
	
class persian_panel_hide(sublime_plugin.WindowCommand):
	def run(self):
		w = self.window
		w.run_command('hide_panel', { 'panel': 'output.persian_panel' })

class persian_async_insert(sublime_plugin.TextCommand):
	def run(self,edit,data):
		w = self.view.window()
		p1=w.find_output_panel('persian_panel')
		if p1!=None:
			lines=p1.lines(sublime.Region(0,p1.size()))
			if len(lines)>100:
				lines100=lines[101:]
				r1=lines[100]

				for itm in lines100:

					r1=r1.cover(itm)

				p1.erase(edit,r1)
			p1.insert(edit,0,data)
			print (data)
		else:
			print (data)

class persian_event(sublime_plugin.EventListener):
	def convert_persian(self,data):
		return algorithm.get_display(pr.reshape(data),'utf-8',True)
	def is_not_panel(self,view):
		if view.window()==None:
			return False
		w=view.window()
		panels=w.panels()
		for pname in panels:
			if pname[:7]=='output.':
				p1=w.find_output_panel(pname[7:])
				if p1.id()==view.id():
					return False
		return True
	def on_selection_modified(self, view):
		if self.is_not_panel(view):
			o1=''
			pre=''
			for itm in view.sel():
				txt=view.substr(view.line(itm))
				o1+=pre
				o1+=txt
				pre='\n'
			po1=self.convert_persian(o1)

			# print(po1)
			view.run_command('persian_async_insert',{'data':po1+'\n'})
		else:
			return False

