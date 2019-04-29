#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:48:19 2019

@author: amal.guha
taggage de fichiers textes contenant des textes bruts, situés dans le dossier corpus.

"""




def tagger(fichier,fichierResultat):
    commande = 'echo '
    commande=commande+ fichier
    commande=commande+ '| /Applications/treetagger/cmd/tree-tagger-french >'+fichierResultat
    return(os.system(commande))

def recupColonne(fichier,n):
   car = ';' #charactère séparateur des colonnes
   txtRetour=''
   fo = open(fichier, "r")
   fo.seek(0)
   for ligne in fo:

        txtRetour=txtRetour+ligne.split(car)[n]+'\n'
   return(txtRetour)

        



#########################################################################
#PROGRAMME PRINCIPAL
#########################################################################

import os
import csv

#paramètres
repProjet = '/anaconda3/envs/DEEIF/'
fichier=repProjet+'corpus/'+'corpus_Adj_comme.csv' #fichier à tagger


#mise dans le répertoire du corpus
os.chdir(repProjet+'corpus')
#print(os.getcwd()) # vérification

#print(os.system('ls -la')) #pour info


texteATagger=recupColonne(fichier,1)
print(tagger(texteATagger,'resu.txt'))




