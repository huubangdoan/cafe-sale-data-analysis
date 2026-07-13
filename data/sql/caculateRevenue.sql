SELECT 
    DATE_FORMAT(`Transaction Date`, '%Y-%m') AS month,
    SUM(`Total Spent`) AS total_revenue,
    COUNT(*) AS num_transactions
FROM cafe_sales_db.cafe_sales
GROUP BY month
ORDER BY month;