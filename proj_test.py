from tkinter import*

class Knjiznica():
    def __init__(self, master):
        menu = Menu(master)
        
        master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label = "Možnosti", menu = file_menu)
        
        file_menu.add_command(label = "Počisti polja", command = self.pocisti_polja)
        file_menu.add_separator()#separator v menuju
        file_menu.add_command(label = "Uvozi predhodne izposoje", command = self.predhodne_izposoje)
        file_menu.add_command(label = "Počisti predhodne izposoje", command = self.pocisti_izposoje)
        file_menu.add_separator()#separator v menuju
        file_menu.add_command(label = "Izhod", command = master.destroy)

        self.prva_vrstica = StringVar(value = "Dobrodošli v Knjižničar 3000!")
        prva_vrstica = Label(master, textvariable = self.prva_vrstica)
        prva_vrstica.grid(row=0, column=0, columnspan=2)
        
        napis_ime = Label(text = " ime avtorja:")
        napis_ime.grid(row=1, column=0)

        self.ime = StringVar(master, value = "")
        ime_polje = Entry(master, textvariable = self.ime)
        ime_polje.grid(row=1, column=1)

        napis_priimek = Label(text = " priimek avtorja:")
        napis_priimek.grid(row=2, column=0)

        self.priimek = StringVar(master, value = "")
        priimek_polje = Entry(master, textvariable = self.priimek)
        priimek_polje.grid(row=2, column=1)
        
        napis_gradivo = Label(text = " gradivo:")
        napis_gradivo.grid(row=3, column=0)
        
        self.gradivo = StringVar(master, value = "")
        gradivo_polje = Entry(master, textvariable = self.gradivo)
        gradivo_polje.grid(row=3, column=1)
        
        self.izpis = StringVar(value = "Vnesi podatke!")
        izpis = Label(master, textvariable = self.izpis)
        izpis.grid(row=4, column=0, columnspan=2)

        gumb = Button(master, text = "Izposodi!", command = self.izposodi)
        gumb.grid(row=5, column = 0, columnspan=2)

    def izposodi(self):
        if len(self.ime.get()) != 0:
            if len(self.priimek.get()) != 0:
                if len(self.gradivo.get()) != 0:
                    self.shrani_izbiro()
                    self.pocisti_polja()
                else:
                     self.ni_vseh_podatkov()
            else:
                self.ni_vseh_podatkov()
        else:
            self.ni_vseh_podatkov()

    def predhodne_izposoje(self):
        #self.izpis.set("Uvažam zgodovino izposoj.")
        self.novo_okno()

    def ni_vseh_podatkov(self):
        self.izpis.set("Vnesi vse potrebne podatke!")

    def pocisti_polja(self):
        self.ime.set("")
        self.priimek.set("")
        self.gradivo.set("")
        self.izpis.set("Vnesi podatke!")

    def pocisti_izposoje(self):
        with open("spomin", "wt", encoding = "utf8") as f:
            f.truncate()

    def shrani_izbiro(self):
        with open("spomin", "a", encoding = "utf8") as f:
            self.pisi_v_datoteko(f)

    def pisi_v_datoteko(self, f):
        print("Avtor: {0} {1}, Naslov: {2}".format(self.priimek.get(),
            self.ime.get(), self.gradivo.get()), file = f)

    def novo_okno(self):
        novo_okno = Toplevel(root)
        novo_okno.title("Seznam dosedanjih izposoj")

        listbox = Listbox(novo_okno)
        listbox.grid(ipadx = 300)

        self.izpis_datoteke(listbox)

    def izpis_datoteke(self, listbox):
        with open("spomin", encoding = "utf8") as f:
            for vrstica in f:
                listbox.insert(END, str(vrstica))

root = Tk()
root.title("Knjižničar 3000")
root.geometry("300x150")
aplikacija = Knjiznica(root)
root.mainloop()
