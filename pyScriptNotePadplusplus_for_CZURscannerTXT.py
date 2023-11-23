
# -*- coding: utf-8 -*-
# Script développé par Thibaud NÉDEY - Tybot.fr
# Ce script permet d'effectuer des remplacements automatiques pour rendre plus lisible un fichier txt généré par l'OCR des scanner CZUR.


# Début de l'action annulable par Ctrl-Z

editor.beginUndoAction()

# Minuscule en fin de ligne et minuscule début de ligne suivante
editor.rereplace(r"([a-z])\r\n([a-z])", r"\1 \2")

editor.rereplace(r"([a-z]) \r\n([a-z])", r"\1 \2")

editor.rereplace(r"([a-z])\r\nà", r"\1 à")
editor.rereplace(r"à\r\n([a-z])", r"à \1")

editor.rereplace(r"([a-z])\r\né", r"\1 é")
editor.rereplace(r"é\r\n([a-z])", r"é \1")

editor.rereplace(r"([a-z])\r\nè", r"\1 è")
editor.rereplace(r"è\r\n([a-z])", r"è \1")

#tiret en fin de ligne et minuscule en début de ligne suivante
editor.rereplace(r"-\r\n([a-z])", r"\1")

#virgule en fin de ligne et minuscule en début de ligne suivante
editor.rereplace(r",\r\n([a-z])", r" \1")

#numéro de page
editor.rereplace(r"\r\n[0-9]+\r\n", r"\r\n\r\n")


# Fin de l'action annulable, Ctrl-Z annulera tous les remplavement précédents
editor.endUndoAction()