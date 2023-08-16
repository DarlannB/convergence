import tkinter as tk
import avion
import main


class Run_graphic():
    def gui_mainloop():
        root = tk.Tk()
        root.minsize=(200,200)
        root.maxsize=(1920,1080)

################################################################### AIRCRAFT POSITION VALUE ####################################################################################

        nomC=tk.Label(root, text="CHASSEUR", font='bold')
        nomC.grid(row=0, column=2)

        ## DECLARATION DES VARIABLES DE TEXT STOCKAGE LABEL CHASSEUR
        llCS=tk.StringVar()
        llCS.set(main.chasseur.latitude)
        lolCS=tk.StringVar()
        lolCS.set(main.chasseur.longitude)
        alCS=tk.StringVar()
        alCS.set(main.chasseur.altitude)

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
        llBS.set(main.bandit.latitude)
        lolBS=tk.StringVar()
        lolBS.set(main.bandit.longitude)
        alBS=tk.StringVar()
        alBS.set(main.bandit.altitude)

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

        ### CONVERGENCE LABEL ###

        convStateVar=tk.StringVar()
        convStateVar.set(main.conv)
        
        ConvStateVar_label=tk.Label(root, textvariable=convStateVar)
        ConvStateVar_label.grid(row=4, column=5)

        def change_text():
            llCS.set(main.chasseur.latitude)
            lolCS.set(main.chasseur.longitude)
            alCS.set(main.chasseur.altitude)
            llBS.set(main.bandit.latitude)
            lolBS.set(main.bandit.longitude)
            alBS.set(main.bandit.altitude)
            convStateVar.set(main.conv)

        def change_statusColor():
            if main.conv == "Divergence":
                ConvStateVar_label.config(bg= "green", fg= "black")
            elif main.conv == "Convergence":
                ConvStateVar_label.config(bg= "red", fg= "black")
            elif main.conv == "Ni convergence ni divergence":
                ConvStateVar_label.config(bg= "gray51", fg= "white")

        button=tk.Button(root, text="RUN CALCULUS", command=lambda:[avion.Avion.deplacement,  main.comparaison(), change_text(), root.update_idletasks(), change_statusColor()])
        button.grid(row=10, column=2)

################################################################### AIRCRAFT BEHAVIOUR VALUE ####################################################################################

        ##CHASSEUR
        nomCb=tk.Label(root, text="CHASSEUR", font='bold')
        nomCb.grid(row=0, column=9)

        heading_labelC=tk.Label(root, text="HDG")
        horizontalSpeed_labelC=tk.Label(root, text="Vx")
        verticalSpeed_labelC=tk.Label(root, text="Vz")
        heading_labelC.grid(row=1, column=8)
        horizontalSpeed_labelC.grid(row=2, column=8)
        verticalSpeed_labelC.grid(row=3, column=8)

        ##BANDIT
        nomBb=tk.Label(root, text="BANDIT", font='bold')
        nomBb.grid(row=4, column=9)

        heading_labelB=tk.Label(root, text="HDG")
        horizontalSpeed_labelB=tk.Label(root, text="Vx")
        verticalSpeed_labelB=tk.Label(root, text="Vz")
        heading_labelB.grid(row=5, column=8)
        horizontalSpeed_labelB.grid(row=6, column=8)
        verticalSpeed_labelB.grid(row=7, column=8)
        

        root.mainloop()