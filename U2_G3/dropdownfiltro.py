#si importa sistema y gi (librerias)
import sys
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gio, GObject, Gtk

#Clase dropdown GObject
class DropDown(GObject.Object):
    __gtype_name__ = 'DropDown'

    def __init__(self, name):
        super().__init__()
        self._name = name

    @GObject.Property
    def name(self):
        return self._name

#clase base de la ventana de la aplicacion
class MainWindow(Gtk.ApplicationWindow):
    # Definicion de como va a ser la ventana
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Parametros base (Tamaño, Titulo)
        self.set_default_size(600, 100)
        self.set_title("Dropdown")
        self.app_ = self.get_application()
        #contenedor base, orientacion
        self.main_vertical_box = Gtk.Box.new( Gtk.Orientation.VERTICAL,10)
        self.set_child(self.main_vertical_box)

        self.search_text = ''

        #lista de datos para el dropdown
        datos_dropdown = ["Ricardo","Francisco","Matias","Alejandro"]

        #crear model con filtro
        self.model_dropdown = Gio.ListStore(item_type=DropDown)
        self.sort_model  = Gtk.SortListModel(model=self.model_dropdown) # FIXME: Gtk.Sorter?
        self.filter_model = Gtk.FilterListModel(model=self.sort_model)
        self.filter = Gtk.CustomFilter.new(self._do_filter_view, self.filter_model)
        self.filter_model.set_filter(self.filter)

        for i in datos_dropdown:
            self.model_dropdown.append(DropDown(name=i))
        #crear factory
        factory_dropdown = Gtk.SignalListItemFactory()
        factory_dropdown.connect("setup", self._on_factory_dropdown_setup)
        factory_dropdown.connect("bind", self._on_factory_dropdown_bind)

        #crear dropdown
        self.dropdown = Gtk.DropDown(model=self.filter_model, factory=factory_dropdown)
        self.dropdown.set_enable_search(True)
        self.main_vertical_box.append(self.dropdown)
        self.dropdown.connect("notify::selected-item", self._on_selected_dropdown)
        
        #botón dropdown
        self.button = Gtk.Button.new_with_label(label="imprimir")
        self.button.connect("clicked",self.on_print_button_clicked,self.dropdown)
        self.main_vertical_box.append(self.button)

        #crear search
        search_entry = self.get_search_entry(self.dropdown)
        search_entry.connect('search-changed', self._on_search_changed)

    def get_search_entry(self, dropdown1):
        popover = dropdown1.get_last_child()
        box = popover.get_child()
        box2 = box.get_first_child()
        search_entry = box2.get_first_child() # Gtk.SearchEntry
        return search_entry

    def _on_search_changed(self, search_entry):
        self.search_text = search_entry.get_text()
        self.filter.changed(Gtk.FilterChange.DIFFERENT)

    def _do_filter_view(self, item, filter_list_model):
        return self.search_text.upper() in item.name.upper()

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

    #funcion imprimir
    def on_print_button_clicked(self,p_button, dropdown):
        print(dropdown.get_selected_item().name)

    #funcion al seleccionar
    def _on_selected_dropdown(self, dropdown, data):
        widget = dropdown.get_selected_item()
        print("Ha selecionado a", widget.name)

#clase app
class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_activate(self):
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(application=self)
            self.win.present()

app = MyApp(application_id="com.myapplicationexample",flags= Gio.ApplicationFlags.FLAGS_NONE)
app.run(sys.argv)
