-- Question 3
SELECT nom
FROM groupes
WHERE style = 'Latin Jazz';

-- Question 4
UPDATE concerts
SET heure_fin = '22h30'
WHERE idconc = 36;

-- Question 5
SELECT nom
FROM groupes
JOIN concerts ON concerts.idgrp = groupes.idgrp
WHERE scene = 1;

-- Question 6
INSERT INTO groupes
VALUES
(15, 'Smooth Jazz Fourplay', 'Free Jazz', 4);
