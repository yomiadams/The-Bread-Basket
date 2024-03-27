#Find out which items are sold most frequently

SELECT Item, COUNT(*) AS Purchase_Count
FROM Bakery
GROUP BY Item
ORDER BY Purchase_Count DESC
LIMIT 10;

#Analyze sales distribution across different parts of the day
#(e.g., morning, afternoon, evening)

SELECT Daypart, COUNT(*) AS Sales_Count
FROM Bakery
GROUP BY Daypart
ORDER BY Sales_Count DESC;

#Determine how sales numbers differ between weekdays and weekends.
SELECT Daytype, COUNT(*) AS Transaction_Count
FROM Bakery
GROUP BY Daytype;

#Find out which items are most popular during weekdays vs. weekends

SELECT Item, Daytype, COUNT(*) AS Purchase_Count
FROM Bakery
GROUP BY Item, Daytype
ORDER BY Daytype, Purchase_Count DESC;

#Observe how the number of transactions varies over time

SELECT DATE(Datetime) AS Date, COUNT(DISTINCT Transaction_no) AS Transaction_Count
FROM Bakery
GROUP BY Date
ORDER BY Date;
