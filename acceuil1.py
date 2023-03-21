# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess
class AuthForm(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Authentification")
        self.set_border_width(10)
        self.set_default_size(700, 500)
        self.set_position(Gtk.WindowPosition.CENTER)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        label = Gtk.Label()
        label.set_text("Veuillez vous connecter ou vous inscrire")
        grid.attach(label, 0, 0, 2, 1)

        connexion_button = Gtk.Button.new_with_label("Connexion")
        connexion_button.connect("clicked", self.on_connexion_button_clicked)
        grid.attach(connexion_button, 0, 1, 1, 1)

        inscription_button = Gtk.Button.new_with_label("Inscription")
        inscription_button.connect("clicked", self.on_inscription_button_clicked)
        grid.attach(inscription_button, 1, 1, 1, 1)

    def on_connexion_button_clicked(self, button):
        connexion_form = ConnexionForm()
        connexion_form.show_all()

    def on_inscription_button_clicked(self, button):
        inscription_form = InscriptionForm()
        inscription_form.show_all()


class ConnexionForm(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Connexion")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        label = Gtk.Label()
        label.set_text("Formulaire de connexion")
        grid.attach(label, 0, 0, 2, 1)

        # Ajouter ici les widgets pour le formulaire de connexion

class ConnexionForm(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Connexion")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        label = Gtk.Label()
        label.set_text("Formulaire de connexion")
        grid.attach(label, 0, 0, 2, 1)

        nom_label = Gtk.Label("Nom d'utilisateur:")
        grid.attach(nom_label, 0, 1, 1, 1)
        self.nom_champ = Gtk.Entry()
        grid.attach(self.nom_champ, 1, 1, 1, 1)

        mdp_label = Gtk.Label("Mot de passe:")
        grid.attach(mdp_label, 0, 2, 1, 1)
        self.mdp_champ = Gtk.Entry()
        self.mdp_champ.set_visibility(False)
        grid.attach(self.mdp_champ, 1, 2, 1, 1)

        show_password_button = Gtk.Button.new_with_label("Afficher/Masquer le mot de passe")
        show_password_button.connect("clicked", self.on_show_password_button_clicked)
        grid.attach(show_password_button, 1, 3, 1, 1)

        connexion_button = Gtk.Button.new_with_label("Se Connecter")
        connexion_button.connect("clicked", self.on_connexion_button_clicked)
        grid.attach(connexion_button, 1, 4, 1, 1)

    def on_show_password_button_clicked(self, button):
        if self.mdp_champ.get_visibility():
            self.mdp_champ.set_visibility(False)
        else:
            self.mdp_champ.set_visibility(True)

    def on_connexion_button_clicked(self, button):
        username = self.nom_champ.get_text()
        password = self.mdp_champ.get_text()

        # Vérification de l'utilisateur
        users = [("user1", "password1"), ("user2", "password2"), ("user3", "password3")]
        if (username, password) in users:
            message = "Connexion réussie!"
        subprocess.call(["python","C:\\msys64\\home\\Adja Fatou DIOP\\menu.py"])
        self.hide()
        # else:
        # message = "Nom d'utilisateur ou mot de passe incorrect."
        
        # Affichage du message dans une boîte de dialogue
        dialog = Gtk.MessageDialog(parent=self, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text=message)
        dialog.run()
        dialog.destroy()


class InscriptionForm(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Inscription")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        # label = Gtk.Label()
        # label.set_text("Formulaire d'inscription")
        # grid.attach(label, 0, 0, 2, 1)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        grid.attach(vbox, 0, 1, 2, 1)

        label = Gtk.Label("INSCRIPTION")
        label.set_markup("<big><b>INSCRIPTION</b></big>")
        vbox.pack_start(label, False, False, 0)

        cadre = Gtk.Frame(label="Informations")
        cadre.set_border_width(5)
        vbox.pack_start(cadre, True, True, 0)

        grid = Gtk.Grid(column_spacing=5, row_spacing=10, margin=10)
        cadre.add(grid)

        nom = Gtk.Label(label="Nom", xalign=0)
        grid.attach(nom, 0, 0, 1, 1)

        nomchamp = Gtk.Entry()
        grid.attach(nomchamp, 1, 0, 1, 1)

        prenom = Gtk.Label(label="Prénom", xalign=0)
        grid.attach(prenom, 0, 1, 1, 1)

        prenomchamp = Gtk.Entry()
        grid.attach(prenomchamp, 1, 1, 1, 1)

        numero = Gtk.Label(label="Numéro", xalign=0)
        grid.attach(numero, 0, 2, 1, 1)

        numerochamp = Gtk.Entry()
        grid.attach(numerochamp, 1, 2, 1, 1)

        role = Gtk.Label(label="Role", xalign=0)
        grid.attach(role, 0, 3, 1, 1)
        degiskenler = ["Gérant", "Responsable"]
        rolechamp = Gtk.ComboBoxText()
        for i in degiskenler:
            rolechamp.append_text(i)
        rolechamp.set_active(0)
        grid.attach(rolechamp, 1, 3, 1, 1)

        email = Gtk.Label(label="Email", xalign=0)
        grid.attach(email, 0, 4, 1, 1)

        emailchamp = Gtk.Entry()
        grid.attach(emailchamp, 1, 4, 1, 1)

        mot_de_passe = Gtk.Label(label="Mot de passe", xalign=0)
        grid.attach(mot_de_passe, 0, 5, 1, 1)

        mot_de_passechamp = Gtk.Entry()
        grid.attach(mot_de_passechamp, 1, 5, 1, 1)

        confirmer_mot_de_passe = Gtk.Label(label="Confirmer votre mot de passe", xalign=0)
        grid.attach(confirmer_mot_de_passe, 0, 6, 1, 1)

        confirmer_mot_de_passechamp = Gtk.Entry()
        grid.attach(confirmer_mot_de_passechamp, 1, 6, 1, 1)

        enregistrer_button = Gtk.Button(label="Enregistrer", margin=10)
        enregistrer_button.connect("clicked", self.on_button_clicked)
        grid.attach(enregistrer_button, 1, 7, 1, 1)

        grid.set_halign(Gtk.Align.CENTER)
        grid.set_valign(Gtk.Align.CENTER)


    def on_button_clicked(self, button):
        print("Le bouton a été cliqué.")

win = AuthForm()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
