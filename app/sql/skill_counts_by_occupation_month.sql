CREATE TABLE IF NOT EXISTS AwsDataCatalog."datalake".skill_counts_by_occupation_and_month AS
SELECT soc.soc6d_title occupation_category,
    date_format(CAST(soc.startdate as DATE), '%m') Month,
    COUNT(skill) skill_count,
    SUM(COUNT(skill)) OVER (PARTITION BY soc.soc6d_title) as total_skill_count_by_occupation,
    CAST(COUNT(skill) as REAL)/CAST(SUM(COUNT(skill)) OVER (PARTITION BY soc.soc6d_title) as REAL) normalized_skill_count_by_occupation
FROM AwsDataCatalog."revelio-glue".positions_soc soc
INNER JOIN AwsDataCatalog."revelio-glue".user_skills skills
ON soc.user_id = skills.user_id
WHERE soc.soc6d_title IS NOT NULL
AND date_format(CAST(soc.startdate as DATE), '%m') IS NOT NULL
AND skill IS NOT NULL
GROUP BY soc.soc6d_title, date_format(CAST(soc.startdate as DATE), '%m')
ORDER BY soc.soc6d_title DESC, Month ASC
