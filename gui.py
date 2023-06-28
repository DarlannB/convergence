import tkinter as tk
import avion
import main

class Application(tk.Tk):
    def __init__(self):
          tk.Tk.__init__(self)
          long=200
          larg=200
          self.size=(long,larg)
          Widgets.boxPositionBandit(self)
          Widgets.boxPostionChasseur(self)
          Widgets.calculusButton(self)

#########################  AFFICHAGE DES INFORMATIONS SANS MODIFICATION  ##########################################
    
class Widgets():#Affichage LAT LONG et Alt pour chasseur     
        def boxPostionChasseur(self):
            frame1=tk.Frame(self)
            frame1.pack()

            self.lat_label=tk.Label(frame1,text="LAT")
            self.long_label=tk.Label(frame1,text="LONG")
            self.alt_label=tk.Label(frame1,text="Alt")
            self.lat_label.grid(row=1, column=1)
            self.long_label.grid(row=2, column=1)
            self.alt_label.grid(row=3, column=1)

            self.lat_label_show=tk.Label(frame1, text=main.chasseur.latitude)
            self.long_label_show=tk.Label(frame1,text=main.chasseur.longitude)
            self.alt_label_show=tk.Label(frame1,text=main.chasseur.altitude)
            self.lat_label_show.grid(row=1, column=2)
            self.long_label_show.grid(row=2, column=2)
            self.alt_label_show.grid(row=3, column=2)

            self.nom=tk.Label(frame1, text="CHASSEUR", font='bold')
            self.nom.grid(row=0, column=0)

        def boxPositionBandit(self): #Affichage LAT LONG et Alt pour bandit
            frame2=tk.Frame(self)
            frame2.pack()

            self.lat_label=tk.Label(frame2,text="LAT")
            self.long_label=tk.Label(frame2,text="LONG")
            self.alt_label=tk.Label(frame2,text="Alt")
            self.lat_label.grid(row=1, column=1)
            self.long_label.grid(row=2, column=1)
            self.alt_label.grid(row=3, column=1)

            self.lat_label_show=tk.Label(frame2, text=main.bandit.latitude)
            self.long_label_show=tk.Label(frame2,text=main.bandit.longitude)
            self.alt_label_show=tk.Label(frame2,text=main.bandit.altitude)
            self.lat_label_show.grid(row=1, column=2)
            self.long_label_show.grid(row=2, column=2)
            self.alt_label_show.grid(row=3, column=2)

            self.nom=tk.Label(frame2, text="BANDIT", font='bold')
            self.nom.grid(row=0, column=0)

         
        def calculusButton(self):
            button=tk.Button(text="RUN CALCULUS")
            button.pack()
            button.config(command=avion.Avion.deplacement and main.comparaison)

        def update_label():
            
            pass