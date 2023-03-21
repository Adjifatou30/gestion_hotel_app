# -*- coding: utf-8 -*-
import gi
import requests

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Communication avec une API Go")
        self.set_border_width(10)

        # Créer une grille pour organiser les widgets
        grid = Gtk.Grid()
        self.add(grid)

        # Ajouter un champ de saisie pour le nom
        label_nom = Gtk.Label(label="Nom:")
        self.nom = Gtk.Entry()
        grid.attach(label_nom, 0, 0, 1, 1)
        grid.attach(self.nom, 1, 0, 1, 1)

        # Ajouter un champ de saisie pour l'adresse
        label_adresse = Gtk.Label(label="Adresse:")
        self.adresse = Gtk.Entry()
        grid.attach(label_adresse, 0, 1, 1, 1)
        grid.attach(self.adresse, 1, 1, 1, 1)

        # Ajouter un bouton pour valider le formulaire
        button = Gtk.Button(label="Valider")
        button.connect("clicked", self.on_button_clicked)
        grid.attach(button, 0, 2, 2, 1)

    def on_button_clicked(self, widget):
        # Récupérer les valeurs saisies par l'utilisateur
        id= self.id.get_text()
        nom = self.nom.get_text()
        prenom = self.prenom.get_text()
        telephone = self.telephone.get_text()
        classe = self.classe.get_text()
        chambre = self.chambre.get_text()
        DateChambre= self.DateChambre.get_text()
        Nuitee = self.Nuitee.get_text()
        DateSortie = self.DateSortie.get_text()
        # Appeler l'API Go avec les données saisies
        url = 'http://localhost:3000//reservations/new'
        data = {'ID':id,'Nom': nom, 'Prenom': prenom,'Telephone':telephone,'Classe':classe,'Chambre':chambre,'DateChambre':DateChambre,'Nuitee':Nuitee,'DateSortie':DateSortie}
        response = requests.post(url, data=data)

        # Vérifier si l'appel a réussi et afficher un message de confirmation
        if response.status_code == 200:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Les données ont été enregistrées avec succès.")
            dialog.run()
            dialog.destroy()
        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Une erreur s'est produite lors de l'enregistrement des données.")
            dialog.run()
            dialog.destroy()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
