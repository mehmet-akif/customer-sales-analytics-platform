-- Total revenue
SELECT SUM(amount) AS total_revenue
FROM orders;

-- Revenue by country
SELECT c.country, SUM(o.amount) AS total_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY total_revenue DESC;

-- Monthly revenue trend
SELECT DATE_TRUNC('month', order_date) AS month, SUM(amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

-- Top 10 customers by lifetime value
SELECT customer_id, SUM(amount) AS lifetime_value
FROM orders
GROUP BY customer_id
ORDER BY lifetime_value DESC
LIMIT 10;

-- Average satisfaction by issue type
SELECT issue_type, AVG(satisfaction_score) AS avg_satisfaction
FROM support_tickets
GROUP BY issue_type
ORDER BY avg_satisfaction DESC;

-- Marketing cost by channel
SELECT channel, SUM(campaign_cost) AS total_cost
FROM marketing_campaigns
GROUP BY channel
ORDER BY total_cost DESC;