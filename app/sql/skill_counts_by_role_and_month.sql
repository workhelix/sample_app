CREATE TABLE IF NOT EXISTS AwsDataCatalog."datalake".skill_counts_by_role_and_month AS
SELECT soc.mapped_role Role,
       date_format(CAST(soc.startdate as DATE), '%m') Month,
       COUNT(skills.skill) skill_count,
       SUM(COUNT(skill)) OVER (PARTITION BY soc.mapped_role) as total_skill_count_by_occupation,
       CAST(COUNT(skill) as REAL)/CAST(SUM(COUNT(skill)) OVER (PARTITION BY soc.mapped_role) as REAL) normalized_skill_count_by_occupation
FROM AwsDataCatalog."revelio-glue".positions_soc soc
INNER JOIN AwsDataCatalog."revelio-glue".user_skills skills
ON soc.user_id = skills.user_id
WHERE soc.mapped_role IS NOT NULL
AND date_format(CAST(soc.startdate as DATE), '%m') IS NOT NULL
AND skill IS NOT NULL
GROUP BY soc.mapped_role, date_format(CAST(soc.startdate as DATE), '%m')
ORDER BY soc.mapped_role DESC, Month ASC
