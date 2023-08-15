-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, ROUND(AVG(temperature), 2) AS avg_temperature
FROM temperatures
GROUP BY city
ORDER BY avg_temperature DESC;
