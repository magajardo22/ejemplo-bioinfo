#importar librerias
import sys
import gi
#version gtk
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GObject
#importar clase Mensaje
from message import Mensaje

#crear clase de la ventana
class MainWindow(Gtk.ApplicationWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #tamaño y titulo
        self.set_default_size(800, 600)
        self.set_title("Guia2")
        #crear widget
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box)
        #crear viñeta
        self.label = Gtk.Label()
        self.label.set_text("Guarda tu texto")
        self.box.append(self.label)
        #crear entrada de texto
        self.texto = Gtk.Entry()     
        self.texto.props.placeholder_text = "Ingrese texto"                                   
        self.box.append(self.texto)
        #crear boton guardado
        self.button_save = Gtk.Button(label="Guardar")
        self.button_save.connect('clicked', self.save)                          
        self.box.append(self.button_save)
        #abrir ventana nativa
        self._native = self.text_save()                   
        self._native.connect("response", self.on_file_save_response) 

    #funcion guardar (nativo)
    def save(self, button):
            self._native.show()

    #funcion guardar respuesta
    def on_file_save_response(self, native, response):
        if response == Gtk.ResponseType.ACCEPT:
            _path = native.get_file().get_path()
            print(_path)
            with open(_path, "w") as _file:
                _file.write(f'{self.texto.get_text()}\n')
            self.open_msn()
                
    #funcion guardar texto
    def text_save(self): 
        return Gtk.FileChooserNative(title="Save File",
                                    # "self.main_window" is defined elsewhere as a Gtk.Window
                                    #transient_for=self.main_window,
                                    action=Gtk.FileChooserAction.SAVE,
                                    accept_label="_Save",
                                    cancel_label="_Cancel",
                                    )
    
    #funcion mensaje
    def open_msn(self):
        msn = Mensaje(parent=self.get_root())
        msn.connect("response", self.on_msn_response)
        msn.set_visible(True) 

    #funcion cerrar mensaje
    def on_msn_response(self, msn, response):
        if response == Gtk.ResponseType.OK:
            print("Presionó OK")
        msn.close()

#Clase de la aplicacion
class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

#Corre el programa
app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
