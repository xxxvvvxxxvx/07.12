import tkinter as tk
window = tk.Tk()

lbl_sasveicinasanas = tk.Label(
text = "Sveiks/a!\nSpēlēsim spēli - akmens, šķēres, papīrīts!",
fg = "blue",
bg = "gray"
)

lbl_izveelies = tk.Label(text = "Izvēlies kādu no zemāk piedāvātajiem
variantiem: ")

btn_akmens = tk.Button(text = "Akmens")
btn_skeres = tk.Button(text = "Šķēres")
btn_papirs = tk.Button(text = "Papīrs")

lbl_lietizv = tk.Label(text = "Tava izvēle: ")
lbl_datizv = tk.Label(text = "Datora izvēle: ")
btn_galarez = tk.Button(text = "Kāds ir rezultāts")

def akmens_izv(event):
lietotajs = "Akmens"
lbl_lietizv["text"] = f"Tava izvēle: {lietotajs}"
def skeres_izv(event):
lietotajs = "Šķēres"

lbl_lietizv["text"] = f"Tava izvēle: {lietotajs}"
def papirs_izv(event):
lietotajs = "Papīrs"
lbl_lietizv["text"] = f"Tava izvēle: {lietotajs}"

def dat_izv():
defizveeles = ['Akmens','Šķēres','Papīrs']
pretIzveele = random.choice(defizveeles)
lbl_datizv["text"] = f"Datora izvēle: {pretIzveele}"

def rezultats(event):
dators = lbl_datizv["text"]
lietotajs = lbl_lietizv["text"]
dators = dators.split()
lietotajs = lietotajs.split()

if dators[2]== lietotajs[2]:
lbl_rezultats["text"] = "Rezultāts: Neizšķirts"
else:
lbl_rezultats["text"] = "Rezultāts: Vēl jāsataisa"
btn_galarez.bind("<Button-1>", rezultats)