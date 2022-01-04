class Morpion:

    def __init__(self):
        self.joueur1 = "X"
        self.joueur2 = "O"
        self.grille = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    def jouer(self, joueur):
        case = input("Entrez votre coup: ")

        case.split(",")
        # 1,2 --> '1','2'
        self.grille[int(case[0])][int(case[2])] = joueur

    def afficher_grille(self):
        for i in range(3):

            print('|'+self.grille[i][0]+'|'+self.grille[i]
                  [1]+'|'+self.grille[i][2]+'|', end="")
            print()

    def test_fin_jeu(self, joueur: str):
        """
        :params:joueur: str ("X" ou "O")
        :returns: joueur si il a gagné. sinon :
                  True si la partie est terminée, False sinon
         """
        if "_" in self.grille[0] or self.grille[1] or self.grille[2]:
            for j in range(3):
                if self.grille[0][j] == self.grille[1][j] and self.grille[1][j] == self.grille[2][j]:
                    if self.grille[0][j] == joueur:
                        return joueur

            for i in range(3):
                if self.grille[i][0] == self.grille[i][1] and self.grille[i][1] == self.grille[i][2]:
                    if self.grille[i][0] == joueur:
                        return joueur

            if self.grille[0][0] == self.grille[1][1] and self.grille[1][1] == self.grille[2][2]:
                if self.grille[0][0] == joueur:

                    return joueur

            if self.grille[0][2] == self.grille[1][1] and self.grille[1][1] == self.grille[2][0]:
                if self.grille[0][2] == joueur:

                    return joueur

            return False
        else:
            return True

    def lancer(self):
        """
       :params: aucun (sauf self évidement)
       :returns:None
       X commence. Tant que la partie n'est pas finie :
             demande la case, joue, test fin de jeu, change de joueur
        """

        while self.test_fin_jeu('X') != True and self.test_fin_jeu('O') != True:

            if self.test_fin_jeu('X') == 'X':
                print(self.afficher_grille())
                return None
            else:
                print(self.afficher_grille())
                self.jouer(self.joueur2)

            if self.test_fin_jeu('O') == 'O':
                print(self.afficher_grille())
                return None
            else:
                print(self.afficher_grille())
                self.jouer(self.joueur1)


jeu = Morpion()
jeu.lancer()


# jeu = Morpion()
# print("Affichage de la grille : ")
# for ligne in jeu.grille:
#     for i in range(3):1,&
#         print(ligne[i], end=' ')
#     print()
# print("joueur 1", jeu.joueur1)
# print("joueur 2", jeu.joueur2)
