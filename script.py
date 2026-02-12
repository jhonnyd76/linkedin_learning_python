#!/usr/bin/env python3

# Aufgabe: Erstellen Sie ein Skript, das die Länge eines Textes analysiert und Informationen darüber liefert.

# Das Skript soll folgende Funktionalität bieten:
# 1. Ein Pflichtargument (positional argument), das einen Text entgegennimmt.
# 2. Ein optionales Argument --details, das zusätzliche Informationen liefert:
#    - Anzahl der Wörter
# 3. Wenn das Argument --details nicht angegeben wird, soll nur die Anzahl der Zeichen ausgegeben werden.

# Beispiel:
# python3 script.py "Dies ist ein Beispieltext." --details
# Ausgabe:
# Zeichen: 27
# Wörter: 5

# Optional: Erweitern Sie das Skript, um auch die Anzahl der Vokale und Konsonanten zu zählen.
import argparse

from script_loesung import characters, sum_consonants

parser = argparse.ArgumentParser(description="Dies ist nur ein kleiner Textlese Bot")

parser.add_argument("text", type=str, help="Text eingeben")
parser.add_argument("--details", action="store_true", help="Anzahl der Wörter, Vokalen und Konsonanten")

args = parser.parse_args()

text = args.text
chars = len(text)
words = len(text.split())

print(f"Anzahl Zeichen im Text: {chars}")
if args.details:
    print(f"Anzahl Wörter: {words}")

    vowels = "aeiouAEIOU"
    sum_vowels = sum(1 for char in text if char in vowels)
    print(f"Anzahl Vokale im Text: {sum_vowels}")

    consonants = "bcdfghjklmnpqrstvwxyz"
    sum_consonants = sum(1 for char in text if char.lower() in consonants)
    print(f"Anzahl Consonants im Text: {sum_consonants}")

