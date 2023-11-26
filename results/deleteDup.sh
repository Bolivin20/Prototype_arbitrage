#!/bin/bash

# Sprawdź, czy podano nazwę pliku jako argument
if [ -z "$1" ]; then
    echo "Podaj nazwę pliku jako argument."
    exit 1
fi

# Wczytaj dane z pliku
file="$1"

# Usuń powielające się linie z pliku (ignorując godzinę)
awk -F',' '!seen[$4]++' "$file" > "$file.tmp"

# Przeniesienie tymczasowego pliku na oryginalny
mv "$file.tmp" "$file"

echo "Usunięto powielające się linie z pliku (ignorując godzinę): $file"
