import tkinter as tk
import avion
import main

"""class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        root=tk.Tk()
        self.minsize=(200,200)
        self.maxsize=(1920,1080)

        self.nomC=tk.Label(text="CHASSEUR", font='bold')
        self.nomC.grid(row=0, column=2)

        self.lat_labelC=tk.Label(text="LAT")
        self.long_labelC=tk.Label(text="LONG")
        self.alt_labelC=tk.Label(text="Alt")
        self.lat_labelC.grid(row=1, column=1)
        self.long_labelC.grid(row=2, column=1)
        self.alt_labelC.grid(row=3, column=1)

        self.lat_label_showC=tk.Label(text=main.chasseur.latitude)
        self.long_label_showC=tk.Label(text=main.chasseur.longitude)
        self.alt_label_showC=tk.Label(text=main.chasseur.altitude)
        self.lat_label_showC.grid(row=1, column=3)
        self.long_label_showC.grid(row=2, column=3)
        self.alt_label_showC.grid(row=3, column=3)

        self.nomB=tk.Label(text="BANDIT", font='bold')
        self.nomB.grid(row=4, column=2)

        self.lat_labelB=tk.Label(text="LAT")
        self.long_labelB=tk.Label(text="LONG")
        self.alt_labelB=tk.Label(text="Alt")
        self.lat_labelB.grid(row=5, column=1)
        self.long_labelB.grid(row=6, column=1)
        self.alt_labelB.grid(row=7, column=1)

        self.lat_label_showB=tk.Label(text=main.bandit.latitude)
        self.long_label_showB=tk.Label(text=main.bandit.longitude)
        self.alt_label_showB=tk.Label(text=main.bandit.altitude)
        self.lat_label_showB.grid(row=5, column=3)
        self.long_label_showB.grid(row=6, column=3)
        self.alt_label_showB.grid(row=7, column=3)

        #Widgets.boxPositionBandit(self)
        #Widgets.boxPostionChasseur(self)

        button=tk.Button(text="RUN CALCULUS")
        button.grid(row=10, column=2)
        button.config(command=avion.Avion.deplacement and main.comparaison and root.update_idletasks())
    def update_labels():
        pass
    
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
class BoxPosition():
    latC=main.chasseur.latitude
    longC=main.chasseur.longitude
    altC=main.chasseur.altitude"""

class Run_graphic():
    def gui_mainloop():
        root = tk.Tk()
        root.minsize=(200,200)
        root.maxsize=(1920,1080)

        nomC=tk.Label(root, text="CHASSEUR", font='bold')
        nomC.grid(row=0, column=2)

        ## DECLARATION DES VARIABLES DE TEXT STOCKAGE LABEL CHASSEUR
        llCS=tk.StringVar()
        llCS.set(main.chasseur.longitude)
        lolCS=tk.StringVar()
        lolCS.set(main.chasseur.altitude)
        alCS=tk.StringVar()
        alCS.set(main.chasseur.latitude)

        lat_labelC=tk.Label(root, text="LAT")
        long_labelC=tk.Label(root, text="LONG")
        alt_labelC=tk.Label(root, text="Alt")
        lat_labelC.grid(row=1, column=1)
        long_labelC.grid(row=2, column=1)
        alt_labelC.grid(row=3, column=1)

        lat_label_showC=tk.Label(root, textvariable=llCS)
        long_label_showC=tk.Label(root, textvariable=lolCS)
        alt_label_showC=tk.Label(root, textvariable=alCS)
        lat_label_showC.grid(row=1, column=3)
        long_label_showC.grid(row=2, column=3)
        alt_label_showC.grid(row=3, column=3)

        nomB=tk.Label(root, text="BANDIT", font='bold')
        nomB.grid(row=4, column=2)
        ## DECLARATION DES VARIABLES DE TEXT STOCKAGE LABEL BANDIT
        llBS=tk.StringVar()
        llBS.set(main.bandit.longitude)
        lolBS=tk.StringVar()
        lolBS.set(main.bandit.altitude)
        alBS=tk.StringVar()
        alBS.set(main.bandit.latitude)

        lat_labelB=tk.Label(root, text="LAT")
        long_labelB=tk.Label(root, text="LONG")
        alt_labelB=tk.Label(root, text="Alt")
        lat_labelB.grid(row=5, column=1)
        long_labelB.grid(row=6, column=1)
        alt_labelB.grid(row=7, column=1)

        lat_label_showB=tk.Label(root, textvariable=llBS)
        long_label_showB=tk.Label(root, textvariable=lolBS)
        alt_label_showB=tk.Label(root, textvariable=alBS)
        lat_label_showB.grid(row=5, column=3)
        long_label_showB.grid(row=6, column=3)
        alt_label_showB.grid(row=7, column=3)

        def change_text():
            llCS.set(main.chasseur.latitude)
            lolCS.set(main.chasseur.longitude)
            alCS.set(main.chasseur.altitude)
            llBS.set(main.bandit.latitude)
            lolBS.set(main.bandit.longitude)
            alBS.set(main.bandit.altitude)

        button=tk.Button(root, text="RUN CALCULUS", command=lambda:[avion.Avion.deplacement,  main.comparaison(), change_text(), root.update_idletasks()])
        button.grid(row=10, column=2)

        root.mainloop()