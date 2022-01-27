CREATE TABLE AwsDataCatalog."datalake".skill_counts_by_role AS
SELECT soc.mapped_role Role,
       COUNT(skills.skill) skill_count
FROM AwsDataCatalog."revelio-glue".positions_soc soc
INNER JOIN AwsDataCatalog."revelio-glue".user_skills skills
ON soc.user_id = skills.user_id
WHERE soc.mapped_role IS NOT NULL
AND skill IS NOT NULL
GROUP BY soc.mapped_role
ORDER BY soc.mapped_role DESC
