SELECT COUNT(TRANS_DATE) AS TRANS_COUNT , SUM(AMOUNT) AS TRANS_TOTAL_AMOUNT ,COUNTRY, DATE_FORMAT(trans_date, '%Y-%m') AS month , SUM(state = 'approved') AS approved_count, SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM TRANSACTIONS
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'),COUNTRY 