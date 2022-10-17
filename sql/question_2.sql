WITH
  cte_transaction AS (
  SELECT
    client_id,
    prod_price,
    prod_qty,
    date,
    prop_id
  FROM
    TRANSACTIONS
  WHERE
    date BETWEEN "2019-01-01"
    AND "2019-12-31" )
SELECT
  cte_transaction.client_id,
  SUM(CASE
      WHEN prod_nom.product_type="MEUBLE" THEN (cte_transaction.prod_price* cte_transaction.prod_qty)
  END
    ) AS ventes_meuble,
  SUM(CASE
      WHEN prod_nom.product_type="DECO" THEN (cte_transaction.prod_price* cte_transaction.prod_qty)
  END
    )AS ventes_deco
FROM
  cte_transaction
LEFT JOIN
  PRODUCT_NOMENCLATURE prod_nom
ON
  cte_transaction.prop_id= prod_nom.product_id
GROUP BY
  client_id