#!/usr/bin/env python
# -*- coding: utf-8 -*-

#IMPORTANTE PARA QUE FUNCIONE CON GTK 3
import gi
import math
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class tut_glade:

	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file("machine_selector.glade")
		self.builder.connect_signals(self)
		self.window = self.builder.get_object("window1")

		#**** Menu ****
    	#Acerca de
		self.aboutdialog = self.builder.get_object("aboutdialog1")

		self.window.show()

	#Cerrar ventana
	def on_window1_destroy(self, object, data=None):
		print "Cerrado desde boton"
		Gtk.main_quit()

	def on_gtk_quit_activate(self, menuitem, data=None):
		print "Cerrado desde menu"
		Gtk.main_quit()

	#Ventana acerca de...
	def on_gtk_about_activate(self, menuitem, data=None):
		print "ventana de ayuda abierta"
		self.response = self.aboutdialog.run()
		self.aboutdialog.hide()

if __name__ == "__main__":
	main = tut_glade()
	Gtk.main()