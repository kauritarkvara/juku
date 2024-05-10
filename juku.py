import random
import tkinter as tk
def suurus():
    global kiri
    kiri.pack(fill="both", expand=True)
def vali():
    kiri.configure(state="normal")
    nali = random.choice(naljad)
    kiri.delete("1.0", "end")
    kiri.insert("1.0", nali)
    kiri.configure(state="disabled")
naljad =[]
naljad.append('Juku kukkus vette. Tuli kalamees ja tõmbas ta välja. Kalamees küsis: "Kas sa ujuda ei oska?" Juku vastas: "Ma oskan küll, aga siin on silt: UJUMINE KEELATUD!"')
naljad.append('Õpetaja küsis Jukult: "Mida su ema kodus teeb?" Juku: "Ei tea." Õpetaja: "Mida sinu isa kodus teeb?" Juku: "Ei tea." Juku läheb koju. Küsib emalt: "Mida sa kodus teed?" Ema vastab: "Praen pankooke moosiga." Juku küsib isalt "Mida sa kodus teed?" Isa vastab: "Loen ajalehte." Juku läheb kooli. Õpetaja küsib: "Mida sinu ema kodus teeb?" Juku vastab: "Praeb ajlehte!" Õpetaja: "Mida sinu isa kodus teeb? Juku: "Loeb ajalehte moosiga"')
naljad.append('"Isa, kas tint on väga kallis?" "Mitte eriti." "Miks siis ema nii kõva kisa tõstis, kui ma potitäie tinti diivani peale kallasin?"')
naljad.append('Matemaatikatunnis püüab õpetaja Jukule lahutamistehet selgitada: "Oletame, et mu laual on viis kärbest ja ma taban üht neist kärbsepiitsaga. Mitu kärbest jääb alles?"Juku mõtleb hetke ja teatab: "See üks, kelle te maha lõite!"')
naljad.append('Üks mees läheb mööda ja küsib koerale lähedal olevalt inimeselt: "Kas teie koer ka hammustab?" Ta vastas: "Ei, ta pole kedagi kunagi hammustanud" Mees silitab teda ettevaatlikult ja koer lööb kihvad sisse. Mees hüüdis: "Te ju ütlesite et teie koer ei hammusta!" "Aga ma ei öelnud et see on minu koer!"')
naljad.append('Koolis on loodusõpetuse tund ja õpetaja küsib: "Mida me saame kanalt?" Lapsed vastavad läbisegi: "Muna, liha." Õpetaja küsib Jukult: "Mida veel? Kus su vanaisa magab?" "Kapi otsas," vastab Juku. "Kas tal padi ka on?" küsib õpetaja uuesti. "Jah," vastab Juku. "Ja mida me saame siis, kui me padja ära lõhume?" küsib õpetaja. "Peksa vanaisalt," vastab Juku rõõmsalt.')
aken = tk.Tk()
aken.title("Juku :D")
kiri = tk.Text(aken)
nupp = tk.Button(aken, text="Paku midagi muud", command=vali)
kiri.pack()
nupp.pack()
kiri.configure(state="disabled")
aken.bind("<Configure>", lambda event: suurus())
vali()
aken.mainloop()
