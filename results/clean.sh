#!/bin/bash

# Sprawdź, czy podano nazwę pliku jako argument
if [ -z "$1" ]; then
    echo "Podaj nazwę pliku jako argument."
    exit 1
fi

# Wczytaj dane z pliku
file="$1"

# Przetwarzanie danych i zapisanie wyniku do tymczasowego pliku
awk -F',' '$6 <= 20 {print}' "$file" > "$file.tmp"

# Przeniesienie tymczasowego pliku na oryginalny
mv "$file.tmp" "$file"

echo "Usunięto linie, w których ostatnia kolumna ma wartość większą od 1000."
