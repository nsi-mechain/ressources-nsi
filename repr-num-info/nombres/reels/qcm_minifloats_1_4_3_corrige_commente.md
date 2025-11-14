# QCM Minifloats 1-4-3 — Corrigé commenté

*Format utilisé : 1 bit signe | 4 bits exposant biaisé (biais = 7) | 3 bits mantisse.*  
*Spéciaux : exp=1111 → ±∞ si mantisse=000, sinon NaN. Dénormaux : exp=0000 → valeur = (0.mantisse)×2^{-6} avec signe.*

| # | Octet / Énoncé | Analyse (résumé) | Réponse |
|---:|:---------------|:------------------|:--------|
| 1 | **01101010** | s=0; exp=1101→13−7=6; mant=010→1,25 ⇒ 1,25×2^6 | **+80** |
| 2 | **10110111** | s=1; exp=0110→6−7=−1; mant=111→1,875 ⇒ −1,875×2^{−1} | **−0,9375** |
| 3 | **00000000** | exp=0000 et mant=000 → zéro | **0** |
| 4 | **10000010** | dénormalisé : s=1; mant=010→0,25 ⇒ −0,25×2^{−6} | **−0,00390625** |
| 5 | **11111010** | exp=1111 et mant≠000 → NaN | **NaN** |
| 6 | **11111000** | exp=1111 et mant=000; s=1 → −∞ | **−∞** |
| 7 | **+210** | parmi les codes proposés, seul **01000010** encode +210 en 1-4-3 | **01000010** |
| 8 | **Un seul NaN ?** (parmi : 11111000, 11111100, 01111000, 11000000, 10000010) | NaN ⇔ exp=1111 et mant≠000 → **11111100** | **11111100** |
| 9 | **Plus petit normalisé positif** | exp min normalisé =0001 (2^{−6}), mant=000→1,0 ⇒ 2^{−6} | **00001000** |
|10 | **Plus grand dénormalisé positif** | exp=0000; mant max=111 ⇒ 0,875×2^{−6} | **00000111** |
|11 | **Nombre total de NaN** | exp=1111 (1) × mant≠000 (7) × signes (2) | **14** |
|12 | **Normalisés positifs (nombre)** | exp∈{0001…1110} (14) × mant (8) × s=0 | **112** |
|13 | **Plus grand flottant codable** | exp=1110→14−7=7; mant=111→1,875 ⇒ 1,875×2^7 | **+240** |
|14 | **Flottant suivant +60₁₀ (01100111₂)** | 01100111₂ = 60,0; successeur ULP suivant ⇒ 60,125 | **+60,125** |

---
**Rappels utiles**  
- Valeur normalisée : (−1)^s × (1+mant/8) × 2^{exp−7}.  
- Valeur dénormalisée : (−1)^s × (mant/8) × 2^{−6}.  
- Zéro : exp=0000, mant=000 (avec signe).  
- ±∞ : exp=1111, mant=000.  
- NaN : exp=1111, mant≠000.

