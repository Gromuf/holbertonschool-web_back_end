-- 3-glam_rock.sql
SELECT band_name, (IFNULL(split, 2024) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam Rock%'
ORDER BY lifespan DESC;
