-- 3-glam_rock.sql
SELECT band_name, (COALESCE(split, YEAR(2024))) - formed AS lifespan
FROM metal_bands
WHERE style = '%Glam Rock%'
ORDER BY lifespan DESC;
