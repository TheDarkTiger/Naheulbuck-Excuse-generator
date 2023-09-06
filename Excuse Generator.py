#!/usr/bin/env python
#! coding: utf-8
#! python3
# Naheulbuck excuse generator
# [TheDarkTiger] 2023

import random

def get_aupif( liste=(0) ) :
	return liste[ random.randrange( 0, len( liste ) ) ]

def get_excuse_bidon() :
	sujets = ("un zombie", "le troll érudit", "l'un des gardiens", "un rat mutant", "l'aubergiste", "le bourreau ivre", "un ménestrel moche", "le gobelin de ménage", "un orque d'élite", "le sorcier stagiaire", "un type suspect", "le prisonier barbu", "l'herboriste", "le chien d'un voisin", "un garde de la ville", "un colporteur", "un aventurier", "le plombier", "l'ingénieur gobelin", "un vieux fou")
	sujet = get_aupif( sujets )
	
	actions = ("a glissé", "a dérapé", "a cassé un bidule", "a brisé un truc", "a vomi", "a perdu ses clés", "a fait ses besoins", "était bloqué", "s'est perdu", "est tombé", "s'est endormi", "a passé la nuit", "s'est réveillé", "s'est tué", "s'est fait mal", "a trébuché", "était coincé", "s'est battu", "a causé des ennuis", "a mis le feu")
	action = get_aupif( actions )
	
	lieux = ("la cave", "le souterrain nord", "le grenier", "mon bureau", "la remise à ingrédients", "les cuisines", "la niche des chiens", "la volière à corbeaux", "la fosse à scorpions", "votre bureau", "l'escalier du deuxième niveau", "le bac du limon glaireux", "le couloir principal", "le hangard de bricolage", "l'atelier de forge", "la salle de fouettage", "le dortoir des orques", "l'antre de Golbargh", "le magasin", "votre bibliothèque")
	lieu = get_aupif( lieux )
	
	adjectifs = ("de cette bête", "de cette stupide", "d'une grosse", "d'une infâme", "d'une étrange", "d'une incroyable", "de l'improbable", "de la fameuse", "de cette imbécile de", "de la ridicule", ",c'est ballot, de la", "de l'existance d'une", "de l'embûche causée par une", "du piège de représentait une", "de la présence de cette", ",vous allez rire, d'une", ",c'est bien dommage, de la", "de la position d'une", "de son penchant pour une", "d'une médiocre")
	adjectif = get_aupif( adjectifs )
	
	causes = ("brouette rouillée", "mannivelle tordue", "scie abîmée", "bassine oubliée", "clé de douze", "corbeille de linge", "hallebarde tordue", "chouette empaillée", "terrine piégée", "flûte empoisonnée", "tête de goule", "faux venimeuse", "guitare disloquée", "bielle biscornue", "salière brisée", "peau de banane", "perruque décrépite", "chaussette rouge", "babouche verte", "pantoufle usée")
	cause = get_aupif( causes )
	
	addendums = ("venait de ma grand-mère", "était justement là", "est apparue comme par magie", "venait de votre cousin", "avait été abandonnée", "était suspecte", "n'aurait pas dû se trouver là", "avait justement l'air fourbe", "était dans l'ombre", "n'avait l'air de rien", "a été laissé par un voisin", "était bel et bien dangeureuse", "était pourtant chère", "avait une odeur inquiétante", "avait changé de place", "aurait dpu être rangée", "vous appartient", "s'est révélée glissante", "était peut-être à moi", "pose toujours des problèmes")
	addendum = get_aupif( addendums )
	
	string = f"Je suis désolé, maître... C'est parceque {sujet} {action} dans {lieu} et tout ça à cause {adjectif} {cause} qui {addendum} donc c'est pas ma faute !"
	
	return string


# Main
for i in range( 5 ) :
	string = get_excuse_bidon()
	print( string+"\n" )
