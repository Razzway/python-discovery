# FIRST PYTHON SCRIPT / MADE IN 20/12/2021 / THIS IS A SIMPLY ENTERTAINMENT :)

# Create & Definite some utils functions
yourAge = "Quel âge as-tu ? "
errorHappened = "Attention ! une erreur est survenue, vous devez précisez un/des chiffre(s) pour l'âge."
def ask_age():
    myAge_precise = 0
    while myAge_precise == 0:
        myAge_str = input(yourAge)
        try:
            myAge_precise = int(myAge_str)
        except:
            print(errorHappened)
    return myAge_precise


yourName = "Comment t'appelles-tu ? "
def ask_name():
    myName_precise = ""
    while myName_precise == "":
        myName_precise = input(yourName)
    return myName_precise


againKid = "Vous êtes encore un enfant."
soonAdult = "Vous êtes bientôt majeur, plus qu'une année !"
barelyAdult = "Vous êtes tout juste une personne majeure."
beforeEighteen = "Vous êtes une personne mineure."
afterEighteen = "Vous êtes une personne majeure."
oldPeople = "Vous êtes bientôt à la retraite."
def show_user_answer(myName, myAge):
    # -> Usage de la concaténation :
    # print(f"Votre nom est", myName, "et vous avez", myAge, "ans !")
    # -> Usage de la chaîne Formatée :
    # print(f"Votre nom est {myName} et vous avez {myAge} ans !")

    # -> Usage de l'ancienne chaîne formatée :
    print("Votre nom est %s et vous avez %s ans !" % (myName, myAge))
    print("L'an prochain, vous aurez %s ans !" % (myAge+1))
    if myAge <= 10:
        print(againKid)
    elif myAge == 17:
        print(soonAdult)
    elif 60 <= myAge <= 65:
        print(oldPeople)
    elif myAge == 18:
        print(barelyAdult)
    elif myAge < 18:
        print(beforeEighteen)
    else:
        print(afterEighteen)



# Ask a password to continue
accessMDP = ""
while not accessMDP == "test":
    accessMDP = input("Quel est le mot de passe ?")


mdpSuccess = "Mot de passe correct, bienvenue dans mon premier programme."
print(mdpSuccess)

masterName = "Razzway"
assistantName = "Ayris"
print("Salut, je suis l'assistant informatique %s le tout premier prototype de %s" % (assistantName, masterName))

# Precise your name to continue
myName = ask_name()
print(myName, "? C'est un joli prénom !")

# Precise your age to continue
myAge = ask_age()

# This is the result of the precedent answer
show_user_answer(myName, myAge)

# HERE IS AN EXAMPLE OF THE BOUCLE FOR
"""
NB_OF_PEOPLE = 4
for i in range(0, NB_OF_PEOPLE):
    myName = "People n°" + str(i+1)
    myAge = ask_age(myName)
    show_user_answer(myName, myAge)
"""






