CREATE TABLE IF NOT EXISTS AwsDataCatalog."datalake".skill_counts_by_occupation_category AS
SELECT soc.soc6d_title occupation_category,
       COUNT(skills.skill) skill_count
FROM AwsDataCatalog."revelio-glue".positions_soc soc
INNER JOIN AwsDataCatalog."revelio-glue".user_skills skills
ON soc.user_id = skills.user_id
WHERE soc.soc6d_title IS NOT NULL
AND skill IS NOT NULL
GROUP BY soc.soc6d_title
ORDER BY soc.soc6d_title DESC
