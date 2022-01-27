CREATE TABLE IF NOT EXISTS AwsDataCatalog."datalake".skill_counts_by_company_and_month AS
SELECT company Company,
    date_format(CAST(soc.startdate as DATE), '%m') Month,
    COUNT(skill) skill_count,
    SUM(COUNT(skill)) OVER (PARTITION BY company) as total_skill_count_by_company,
    CAST(COUNT(skill) as REAL)/CAST(SUM(COUNT(skill)) OVER (PARTITION BY company) as REAL) normalized_skill_count_by_company
FROM AwsDataCatalog."revelio-glue".positions_soc soc
INNER JOIN AwsDataCatalog."revelio-glue".user_skills skills
ON soc.user_id = skills.user_id
WHERE date_format(CAST(soc.startdate as DATE), '%m') IS NOT NULL
AND skill IS NOT NULL
GROUP BY Company, date_format(CAST(soc.startdate as DATE), '%m')
ORDER BY Company DESC, date_format(CAST(soc.startdate as DATE), '%m') ASC
