# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import persian.bidi
import persian.persian_reshaper as pr
from persian.bidi import algorithm

class p1(sublime_plugin.WindowCommand):
	def run(self):
		w = self.window
		p2=w.create_output_panel('test')
		print(dir(p2))
		print(w.panels())
class p2(sublime_plugin.WindowCommand):
	def run(self):
		w = self.window
		w.run_command('show_panel', { 'panel': 'output.test' })
		p3=w.get_output_panel('test')
		p3.run_command("insert",{"characters": "Hello"})
class p3(sublime_plugin.EventListener):
	def on_selection_modified(self, view):
		w = view.window()
		if w!=None:
			p3=w.get_output_panel('test')
			# print(dir(view))
			# print(dir(view.sel()))
			l1={}
			l2=[]
			for itm in view.sel():
				if str(itm) in l1:
					continue
				txt=view.substr(view.line(itm))
				l1[str(itm)]=txt
				l2.append(str(itm))
			o1=''
			pre=''
			for itm in l2:
				o1+=pre
				o1+=l1[itm]
				pre='\n'
			t1=pr.reshape(o1)
			t2=algorithm.get_display(t1,'utf-8',True)
			print(t2)

			# p3.run_command("insert",{"characters": t2})

