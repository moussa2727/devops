import tkinter as tk
from tkinter import ttk, messagebox

class ConvertisseurDevises:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertisseur de Devises")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        # Taux de change (1 euro comme base)
        self.taux = {
            "Euro": 1,
            "Dirham (MAD)": 11.0,
            "CFA (XOF)": 655.96
        }
        
        self.devise1 = tk.StringVar(value="Euro")
        self.devise2 = tk.StringVar(value="Dirham (MAD)")
        self.montant1 = tk.StringVar()
        self.montant2 = tk.StringVar()
        
        self.setup_ui()
    
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill="both", expand=True)
        
        # Titre
        title = ttk.Label(main_frame, text="Convertisseur de Devises", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Section 1
        frame1 = ttk.LabelFrame(main_frame, text="Convertir depuis", padding="10")
        frame1.pack(fill="x", pady=5)
        
        ttk.Label(frame1, text="Devise:").grid(row=0, column=0, sticky="w", pady=5)
        devise1_combo = ttk.Combobox(frame1, textvariable=self.devise1, 
                                    values=list(self.taux.keys()), state="readonly", width=20)
        devise1_combo.grid(row=0, column=1, pady=5, padx=10)
        devise1_combo.bind("<<ComboboxSelected>>", lambda e: self.convertir_1_vers_2())
        
        ttk.Label(frame1, text="Montant:").grid(row=1, column=0, sticky="w", pady=5)
        entry1 = ttk.Entry(frame1, textvariable=self.montant1, width=23)
        entry1.grid(row=1, column=1, pady=5, padx=10)
        entry1.bind("<KeyRelease>", lambda e: self.convertir_1_vers_2())
        
        # Section 2
        frame2 = ttk.LabelFrame(main_frame, text="Convertir vers", padding="10")
        frame2.pack(fill="x", pady=5)
        
        ttk.Label(frame2, text="Devise:").grid(row=0, column=0, sticky="w", pady=5)
        devise2_combo = ttk.Combobox(frame2, textvariable=self.devise2, 
                                    values=list(self.taux.keys()), state="readonly", width=20)
        devise2_combo.grid(row=0, column=1, pady=5, padx=10)
        devise2_combo.bind("<<ComboboxSelected>>", lambda e: self.convertir_1_vers_2())
        
        ttk.Label(frame2, text="Montant:").grid(row=1, column=0, sticky="w", pady=5)
        entry2 = ttk.Entry(frame2, textvariable=self.montant2, width=23, state="readonly")
        entry2.grid(row=1, column=1, pady=5, padx=10)
        
        # Bouton inverser
        btn_inverser = ttk.Button(main_frame, text="Inverser les devises", command=self.inverser)
        btn_inverser.pack(pady=10)
        
        # Informations taux
        info_frame = ttk.LabelFrame(main_frame, text="Taux de change", padding="10")
        info_frame.pack(fill="x", pady=5)
        
        self.info_label = ttk.Label(info_frame, text="", font=("Arial", 9))
        self.info_label.pack()
        self.mettre_a_jour_info()
    
    def convertir_1_vers_2(self):
        """Convertit de devise1 vers devise2"""
        try:
            montant = float(self.montant1.get())
            taux1 = self.taux[self.devise1.get()]
            taux2 = self.taux[self.devise2.get()]
            
            # Convertir en euro d'abord, puis dans la devise cible
            en_euro = montant / taux1
            resultat = en_euro * taux2
            
            self.montant2.set(f"{resultat:.2f}")
        except ValueError:
            self.montant2.set("")
    
    def inverser(self):
        """Inverse les deux devises"""
        devise_temp = self.devise1.get()
        self.devise1.set(self.devise2.get())
        self.devise2.set(devise_temp)
        
        montant_temp = self.montant1.get()
        self.montant1.set(self.montant2.get())
        self.montant2.set(montant_temp)
        
        self.mettre_a_jour_info()
    
    def mettre_a_jour_info(self):
        """Met à jour les informations des taux"""
        d1 = self.devise1.get()
        d2 = self.devise2.get()
        
        taux1 = self.taux[d1]
        taux2 = self.taux[d2]
        
        # Taux de conversion direct
        taux_direct = taux2 / taux1
        
        self.info_label.config(
            text=f"1 {d1} = {taux_direct:.4f} {d2}\n"
                 f"1 Euro = {self.taux['Dirham (MAD)']:.2f} MAD | "
                 f"1 Euro = {self.taux['CFA (XOF)']:.2f} CFA"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = ConvertisseurDevises(root)
    root.mainloop()