import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GObject
#Clase mensaje
class Mensaje(Gtk.MessageDialog):
    def __init__(self, parent):
        super().__init__(title="Mensaje guardado exitosamente", transient_for=parent)
        self.set_markup("Presione OK para continuar")
        self.add_buttons(                                                       
            "_OK",                                                              
            Gtk.ResponseType.OK
        )