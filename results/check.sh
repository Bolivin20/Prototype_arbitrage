#!/bin/bash

# Sprawdź, czy podano nazwę pliku jako argument
if [ -z "$1" ]; then
    echo "Podaj nazwę pliku jako argument."
    exit 1
fi

# Wczytaj dane z pliku
file="$1"

# Przetwarzanie danych
awk -F',' '$5 > 1000 {print}' "$file"
