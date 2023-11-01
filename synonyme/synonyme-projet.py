from synonyme_module import synonyme

parole = input("Quels sont les paroles de la chanson ? ")
mots = parole.split()  # Split les mots de la chaîne saisie
print("Les mots de la chanson sont : ", mots)
paroleMod = ""
for i in range(len(mots)):
    if len(mots[i]) > 3: 
        syn = synonyme(mots[i])
        paroleMod += syn + " "
    else:
        paroleMod += mots[i] + " "
print(paroleMod)
