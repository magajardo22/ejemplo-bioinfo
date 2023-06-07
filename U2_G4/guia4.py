import gi
import pathlib

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gtk, Gio, Pango, GObject

Adw.init()

class DropDown(GObject.Object):
    __gtype_name__ = 'DropDown'

    def __init__(self, name):
        super().__init__()
        self._name = name

    @GObject.Property
    def name(self):
        return self._name

class ExampleWindow(Gtk.ApplicationWindow):
    elementos = [ ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Guia4')
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))
        self.set_size_request(width=int(1366 / 2), height=int(768 / 2))

        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)

        menu_button_model = Gio.Menu()
        menu_button_model.append('About', 'app.about')

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        header_bar.pack_end(child=menu_button)

        self.vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.vbox1.set_homogeneous(homogeneous=True)
        self.set_child(child=self.vbox1)

        button = Gtk.Button.new_with_label(label="abrir carpeta")
        button.connect('clicked', self.open)
        self.vbox1.append(button)

        self._native2 = self.dialog_open()                                       
        self._native2.connect("response", self.on_file_open_response)            
        
    #model
        self.model_dropdown = Gio.ListStore(item_type=DropDown)
        
        #crear factory
        factory_dropdown = Gtk.SignalListItemFactory()
        factory_dropdown.connect("setup", self._on_factory_dropdown_setup)
        factory_dropdown.connect("bind", self._on_factory_dropdown_bind)

        #crear dropdown
        self.dropdown = Gtk.DropDown(model=self.model_dropdown, factory=factory_dropdown)
        self.dropdown.set_enable_search(True)
        self.vbox1.append(self.dropdown)
        self.dropdown.connect("notify::selected-item", self._on_selected_dropdown)
        

    #funcion factory setup
    def _on_factory_dropdown_setup(self, factory, list_item):
        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label()
        box.append(label)
        list_item.set_child(box)

    #funcion factory bind
    def _on_factory_dropdown_bind(self, factory, list_item):
        box = list_item.get_child()
        label = box.get_first_child()
        method = list_item.get_item()
        label.set_text(method.name)

    #funcion al seleccionar
    def _on_selected_dropdown(self, dropdown, data):
        widget = dropdown.get_selected_item()
        print("Ha selecionado a", widget.name)

    def open(self, button):
        self._native2.show()

    def on_file_open_response(self, native, response):
        if response == Gtk.ResponseType.ACCEPT:
            _path = native.get_file().get_path()
        _path = pathlib.Path(_path)
        archivos_mol = [fichero.name for fichero in _path.iterdir() if _path.glob ("*.mol" )]
        for i in archivos_mol:
            a = i.split(".mol")
            self.model_dropdown.append(DropDown(name=a[0]))

    def dialog_open(self): 
        return Gtk.FileChooserNative(title="Open Folder",
                                    transient_for=self.get_root(),
                                    action=Gtk.FileChooserAction.SELECT_FOLDER,
                                    accept_label="_Open",
                                    cancel_label="_Cancel",
                                    )

    


class ExampleApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='cl.com.Example',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.create_action('quit', self.exit_app, ['<primary>q'])
        self.create_action('about', self.on_about_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ExampleWindow(application=self)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def on_about_action(self, action, param):
        self.about=Gtk.AboutDialog.new()
        self.about.set_authors(["Matias Gajardo"])
        self.about.set_program_name("Visor de Moleculas")
        self.about.set_visible(True)

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)

if __name__ == '__main__':
    import sys

    app = ExampleApplication()
    app.run(sys.argv)