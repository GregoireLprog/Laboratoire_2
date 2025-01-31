#demander a l'utilisateur la somme en euros
euros = float(input("Entrez la somme en euros: "))
#proposer la devise dans laquelle convertir
choix = input("Entrez la devise dans laquelle convertir (USD, GBP, JPY, CNY): ")
#dictionnaire des taux de change
taux = {"USD": 1.1, "GBP": 0.84, "JPY": 160, "CNY": 7.5}
USD = 1
GBP = 2
JPY = 3
CNY = 4
#l'utilisateur choisit la devise dans laquelle convertir
print("1. USD")
print("2. GBP") 
print("3. JPY") 
print("4. CNY")
choix = float(input("Entrez le numéro de la devise dans laquelle convertir: "))
print("Résultat:", euros * taux[choix])