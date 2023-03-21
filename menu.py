# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gtk, GdkPixbuf
import test3
import reservation
class FenetreApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="MenuItem Demo")
        self.set_size_request(840, 580)
        grid = Gtk.Grid()
        self.add(grid)

        menubar = Gtk.MenuBar()
        menubar.set_hexpand(True)
        grid.attach(menubar, 0, 0, 1, 1)
        
        #Header Bar
        headerbar = Gtk.HeaderBar()
        headerbar.set_title("Logiciel de Gestion d'Hotel")
        #headerbar.set_subtitle("HeaderBar Subtitle")
        headerbar.set_show_close_button(True)
        self.set_titlebar(headerbar)

        # button = Gtk.Button("Open")
        # headerbar.pack_start(button)
        
        #Menu Gestion de l'hotel
        menuitem_edit = Gtk.MenuItem(label="EDITION")
        menubar.append(menuitem_edit)
        
        #Sous menu Gestion de l'hotel
        submenu_edit = Gtk.Menu()
        menuitem_edit.set_submenu(submenu_edit)
        menuitem_open = Gtk.MenuItem(label="Modifier le nom de l'hotel")
        submenu_edit.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
        menuitem_open = Gtk.MenuItem(label="Modifier les tarifs")
        submenu_edit.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
        menuitem_open = Gtk.MenuItem(label="Reinitialiser Hotel")
        submenu_edit.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)  
        menuitem_quit = Gtk.MenuItem(label="Quit")
        submenu_edit.append(menuitem_quit)
        menuitem_quit.connect('activate', self.on_menu_quit)
        
        #Les Chambres
        menuitem_chambre = Gtk.MenuItem(label="LES CHAMBRES")
        menubar.append(menuitem_chambre)

        #Sous menu Chambres
        
        submenu_chambre = Gtk.Menu()
        menuitem_chambre.set_submenu(submenu_chambre)
        menuitem_open = Gtk.MenuItem(label="LISTES DES CHAMBRES")
        submenu_chambre.append(menuitem_open)
        menuitem_open.connect('activate', self.liste_des_chambres)
        menuitem_open = Gtk.MenuItem(label="CHAMBRES LIBRES")
        submenu_chambre.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
        menuitem_open = Gtk.MenuItem(label="CHAMBRES OCCUPEES")
        submenu_chambre.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
        menuitem_open = Gtk.MenuItem(label="CHAMBRES RESERVEES")
        submenu_chambre.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
        menuitem_open = Gtk.MenuItem(label="CLASSE D'UNE CHAMBRE")
        submenu_chambre.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
         
        menuitem_quit = Gtk.MenuItem(label="Quit")
        submenu_chambre.append(menuitem_quit)
        menuitem_quit.connect('activate', self.on_menu_quit)
        
        
        #les Clients
        menuitem_client = Gtk.MenuItem(label="LES CLIENTS")
        menubar.append(menuitem_client)
        
        #Sous menu les clients
        submenu_client = Gtk.Menu()
        menuitem_client.set_submenu(submenu_client)
        menuitem_open = Gtk.MenuItem(label="LISTES DES CLIENTS")
        submenu_client.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
        menuitem_open = Gtk.MenuItem(label="CLIENTS QUI SORTENT AUJOURD'HUI")
        submenu_client.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
        menuitem_open = Gtk.MenuItem(label="LISTES DES CLIENTS RESERVES")
        submenu_client.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
        menuitem_open = Gtk.MenuItem(label="CLIENTS QUI SONT DANS L'HOTEL")
        submenu_client.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
        menuitem_open = Gtk.MenuItem(label="SUPPRESSION CLIENT")
        submenu_client.append(menuitem_open)
        menuitem_open.connect('activate', self.on_menu_open)
         
        menuitem_quit = Gtk.MenuItem(label="Quit")
        submenu_client.append(menuitem_quit)
        menuitem_quit.connect('activate', self.on_menu_quit)
        
               
        #Menu Reservation
        menuitem_reserv = Gtk.MenuItem(label="RESERVATION")
        menubar.append(menuitem_reserv)
        
        #Sous menu Reservations
        submenu_reserv = Gtk.Menu()
        menuitem_reserv.set_submenu(submenu_reserv)
        menuitem_listReserv = Gtk.MenuItem(label="LISTE DES RESERVATIONS")
        submenu_reserv.append(menuitem_listReserv)
        menuitem_listReserv.connect('activate', self.on_menu_open)
        menuitem_annulReserv = Gtk.MenuItem(label="ANNULER UNE RESERVATION")
        submenu_reserv.append(menuitem_annulReserv)
        menuitem_annulReserv.connect('activate', self.on_menu_open)
        menuitem_ajoutReserv = Gtk.MenuItem(label="AJOUTER UNE RESERVATION")
        submenu_reserv.append(menuitem_ajoutReserv)
        menuitem_ajoutReserv.connect('activate', self.ajouter_reservation)
         
        menuitem_quit = Gtk.MenuItem(label="Quit")
        submenu_reserv.append(menuitem_quit)
        menuitem_quit.connect('activate', self.on_menu_quit)
        
        #Menu Factures
        menuitem_fact = Gtk.MenuItem(label="FACTURES")
        menubar.append(menuitem_fact)
        
        #Menu Statististat
        menuitem_stat = Gtk.MenuItem(label="STATISTIQUES")
        menubar.append(menuitem_stat)
        
        menuitem_quit = Gtk.MenuItem(label="LOGOUT")
        menubar.append(menuitem_quit)
        menuitem_quit.connect('activate', self.on_menu_quit)
        
        
        #Creer un formulaire pour ajouter une reservation

    def ajouter_reservation(self, widget):
        reservation.ReservationForm(self)
    
    def liste_des_chambres(self, widget):
        test3.ChambresWindow(self)
        
    #Ajout de sous menu
    def on_menu_open(self, widget):
        print("add file open dialog")
        
    def on_menu_quit(self, widget):
        Gtk.main_quit()


win = FenetreApp()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()