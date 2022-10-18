

WITH
  RECURSIVE date_selection AS (
  SELECT
    DATE('2019-01-01') AS date_day
  UNION ALL
  SELECT
    DATE_ADD(date_day,INTERVAL 1 day)
  FROM
    date_selection
  WHERE
    date_day < DATE("2019-12-31") )
SELECT
  ds.date AS date,
  IFNULL(SUM( ts.prod_price* ts.prod_qty),0) AS ventes
FROM
  date_selection ds
LEFT JOIN
  TRANSACTIONS ts
ON
  ds.date=ts.date
GROUP BY
  ds.date
order by date asc
