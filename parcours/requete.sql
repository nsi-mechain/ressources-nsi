WITH
-- Associe à chaque point la direction numérique (0=N, 1=NNE, ..., 15=NNO)
caps AS (
    SELECT
        id, cap, distance,
        CASE cap
            WHEN 'N'   THEN 0
            WHEN 'NNE' THEN 1
            WHEN 'NE'  THEN 2
            WHEN 'ENE' THEN 3
            WHEN 'E'   THEN 4
            WHEN 'ESE' THEN 5
            WHEN 'SE'  THEN 6
            WHEN 'SSE' THEN 7
            WHEN 'S'   THEN 8
            WHEN 'SSO' THEN 9
            WHEN 'SO'  THEN 10
            WHEN 'OSO' THEN 11
            WHEN 'O'   THEN 12
            WHEN 'ONO' THEN 13
            WHEN 'NO'  THEN 14
            WHEN 'NNO' THEN 15
            ELSE NULL
        END AS cap_num
    FROM points
),

-- Table des couples consécutifs (pour les changements de cap)
paires AS (
    SELECT
        c1.id AS id,
        c1.cap_num AS cap1,
        c2.cap_num AS cap2
    FROM caps c1
    JOIN caps c2 ON c2.id = c1.id + 1
    WHERE c1.cap_num IS NOT NULL AND c2.cap_num IS NOT NULL
)

SELECT
    (SELECT COUNT(*) FROM points) AS nb_points,
    ROUND(SUM(distance), 2) AS distance_totale,
    -- Virages à droite : delta de cap dans le sens horaire (cap2 - cap1) mod 16 entre 1 et 7
    SUM(CASE
        WHEN ((cap2 - cap1 + 16) % 16) BETWEEN 1 AND 7 THEN 1 ELSE 0 END
    ) AS nb_virages_droite,
    -- Virages à gauche : delta de cap dans le sens antihoraire (cap1 - cap2) mod 16 entre 1 et 7
    SUM(CASE
        WHEN ((cap1 - cap2 + 16) % 16) BETWEEN 1 AND 7 THEN 1 ELSE 0 END
    ) AS nb_virages_gauche
FROM caps
LEFT JOIN paires ON caps.id = paires.id;

