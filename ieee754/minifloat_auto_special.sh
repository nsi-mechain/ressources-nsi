#!/bin/bash

# Script universel mini-float avec gestion des cas spéciaux IEEE754
# Usage : ./minifloat_auto_special.sh "s e...e m...m"

IFS=' ' read -r s e m <<< "$1"

exp_size=${#e}
mant_size=${#m}

# Signe
if [ "$s" -eq 0 ]; then
    sign=1
else
    sign=-1
fi

# Conversion exposant et mantisse
exp=$((2#$e))
mant=$((2#$m))

bias=$(( (2**(exp_size-1)) - 1 ))  # biais IEEE754 standard

# Générer chaînes pour tous 0 et tous 1
all_zeros_e=$(printf "%0${exp_size}d" 0)
all_ones_e=$(printf "%0${exp_size}d" | tr '0' '1')
all_zeros_m=$(printf "%0${mant_size}d" 0)

result=""
if [[ "$e" == "$all_zeros_e" && "$m" == "$all_zeros_m" ]]; then
    # Zéro
    if [ "$sign" -eq 1 ]; then
        result="0"
    else
        result="-0"
    fi
elif [[ "$e" == "$all_ones_e" && "$m" == "$all_zeros_m" ]]; then
    # Infini
    if [ "$sign" -eq 1 ]; then
        result="+inf"
    else
        result="-inf"
    fi
elif [[ "$e" == "$all_ones_e" && "$m" != "$all_zeros_m" ]]; then
    # NaN
    result="NaN"
else
    # Nombre normalisé
    fraction=$(echo "scale=8; 1 + $mant / (2^$mant_size)" | bc -l)
    exp_val=$((exp - bias))
    value=$(echo "scale=8; $sign * $fraction * (2 ^ $exp_val)" | bc -l)
    result="$value"
fi

echo "Entrée         : $s $e $m"
echo "Signe          : $sign"
echo "Exposant       : $exp (binaire $e), taille $exp_size"
echo "Mantisse       : $mant (binaire $m), taille $mant_size"
echo "Valeur décimale: $result"
