SELECT 
    Item,
    SUM(Quantity) AS total_quantity_sold,
    SUM(`Total Spent`) AS total_revenue
FROM cafe_sales
GROUP BY Item
ORDER BY total_quantity_sold DESC
LIMIT 10;