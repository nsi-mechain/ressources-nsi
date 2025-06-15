#!/bin/bash

# Usage: ./convert_all_minifloats.sh 1 4 3

if [ $# -ne 3 ]; then
    echo "Usage: $0 taille_signe taille_exposant taille_mantisse"
    exit 1
fi

taille_signe=$1
taille_exposant=$2
taille_mantisse=$3

total_bits=$((taille_signe + taille_exposant + taille_mantisse))
max_val=$((2**total_bits))

for ((i=0; i<max_val; i++)); do
    # binaire sur le bon nombre de bits
    bin=$(printf "%0${total_bits}d" "$(echo "obase=2; $i" | bc)")
    s=${bin:0:taille_signe}
    e=${bin:taille_signe:taille_exposant}
    m=${bin:taille_signe+taille_exposant:taille_mantisse}
    # Formater pour l'autre script ("s e...e m...m")
    entry="$s $e $m"
    ./minifloat_auto_special.sh "$entry"
    echo "---------------------------------"
done
