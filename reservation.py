# -*- coding: utf-8 -*-
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from datetime import datetime

class ReservationForm(Gtk.Window):
    def __init__(self, ajoutreserv):
        self.ajoutreserv=ajoutreserv
        Gtk.Window.__init__(self, title="Reservation Form")
        self.set_border_width(10)

        # Create grid to hold form elements
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        ID_label = Gtk.Label("ID")
        self.ID_entry = Gtk.Entry()
        grid.attach(ID_label, 0, 0, 1, 1)
        grid.attach(self.ID_entry, 1, 0, 1, 1)
        # Add name field
        name_label = Gtk.Label("Nom")
        self.name_entry = Gtk.Entry()
        grid.attach(name_label, 0, 1, 1, 1)
        grid.attach(self.name_entry, 1, 1, 1, 1)

        # Add last name field
        last_name_label = Gtk.Label("Prenom")
        self.last_name_entry = Gtk.Entry()
        grid.attach(last_name_label, 0, 2, 1, 1)
        grid.attach(self.last_name_entry, 1, 2, 1, 1)

        # Add phone number field
        phone_number_label = Gtk.Label("telephone")
        self.phone_number_entry = Gtk.Entry()
        grid.attach(phone_number_label, 0, 3, 1, 1)
        grid.attach(self.phone_number_entry, 1, 3, 1, 1)

        # Add class field
        class_label = Gtk.Label("Classe")
        self.class_entry = Gtk.Entry()
        grid.attach(class_label, 0, 4, 1, 1)
        grid.attach(self.class_entry, 1, 4, 1, 1)

        # Add room field
        room_label = Gtk.Label("Chambre")
        self.room_entry = Gtk.Entry()
        grid.attach(room_label, 0, 5, 1, 1)
        grid.attach(self.room_entry, 1, 5, 1, 1)

        # Add nights field
        nights_label = Gtk.Label("Nuitée")
        self.nights_entry = Gtk.Entry()
        grid.attach(nights_label, 0, 6, 1, 1)
        grid.attach(self.nights_entry, 1, 6, 1, 1)

        # Add start date field
        start_date_label = Gtk.Label("Date d'entrée")
        self.start_date_entry = Gtk.Entry()
        grid.attach(start_date_label, 0, 7, 1, 1)
        grid.attach(self.start_date_entry, 1, 7, 1, 1)


        # Add end date field
        end_date_label = Gtk.Label("Date de sortie")
        self.end_date_entry = Gtk.Entry()
        grid.attach(end_date_label, 0, 8, 1, 1)
        grid.attach(self.end_date_entry, 1, 8, 1, 1)

        # Add submit button
        self.submit_button = Gtk.Button.new_with_label("Submit")
        self.submit_button.connect("clicked", self.on_submit_clicked)
        grid.attach(self.submit_button, 0, 9, 2, 1)

        # Initialize error message label
        self.error_label = Gtk.Label()
        grid.attach(self.error_label, 0, 10, 2, 1)
        
        self.show_all()

    def on_submit_clicked(self, button):
        name = self.name_entry.get_text()
        last_name = self.last_name_entry.get_text()
        phone_number = self.phone_number_entry.get_text()
        start_date = self.start_date_entry.get_text()
        end_date = self.end_date_entry.get_text()
    
# Convert start date and end date to datetime objects
        try:
            start_date = datetime.strptime(self.start_date_entry.get_text(), "%Y-%m-%d")
            end_date = datetime.strptime(self.end_date_entry.get_text(), "%Y-%m-%d")
        except ValueError:
            self.error_label.set_text("Les dates ne sont pas dans le format correct (année-mois-jour)")
            return
        # Check if start date is before end date
        if start_date > end_date:
            self.error_label.set_text("La date de début ne peut pas être après la date de fin")
        else:
            self.error_label.set_text("Formulaire envoyé avec succès")
        self.show_all()
# win = ReservationForm()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()
