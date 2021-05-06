-- UPDATING/INSERTING ROWS
-- NOTE: pd.merge == psql UPSERT
INSERT INTO Table1 (column1,column2,column3)
SELECT DISTINCT ON (t2.pkey) *
FROM Table2 AS t2
WHERE pkey = t2.pkey
	AND pkey IS NOT NULL
ON CONFLICT (pkey) DO UPDATE 
	SET
    column1= EXCLUDED.column1,
    column2= EXCLUDED.column2,
    column3= EXCLUDED.column2;

-- CHECK RANDOM ROW
-- SELECT * FROM Table1 WHERE pkey='xxxxx'

-- Eliminate duplicates
-- SELECT FROM Table1
-- 	WHERE pkey NOT IN
-- 	(
-- 		SELECT MAX(pkey) as MaxID
-- 		FROM Table1
-- 		GROUP BY pkey);
