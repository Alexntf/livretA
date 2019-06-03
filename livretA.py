def livra():
    
    somme = float(input("Cb d'oseilles voulez-vous poser ? "))
    if somme < 0:
      raise ValueError("Vous ne pouvez pas investir une somme négative")
    elif somme == 0:
      raise ValueError("Vous ne pouvez pas investir une somme nulle")
      
    interet = input("Quel taux d'intêret ? en chiffre décimal stp ")
    
    if "%" in interet:
      raise ValueError("Chiffre décimal ente 0 et 1")  
    else:
      interet = float(interet)
      
      if interet < 0.0:
        raise ValueError("Un taux d'intêret positif serait préférable \n  Tu veux perdre de l'argent ou quoi ?")
          
    annee = int(input("Combien d'année dans la banque ton oseille frero?"))
    if annee <0:
      raise ValueError("Maintenant tu veux remonter le temps ? \n le mec s'est pris pour Docteur Strange")
    elif annee < 1:
      raise ValueError("Tu ne veux pas attendre un peu ?\n la patience est une grande vertue")
    
    total = somme*(1+interet)**(annee)
    print("Vous allez gagner {:.2f}€ pour kiffer !".format(total))
  

     
livra()