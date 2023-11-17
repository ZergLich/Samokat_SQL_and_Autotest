SELECT	c.login, 
	COUNT(o."inDelivery")
FROM "Couriers" AS c 
FULL OUTER JOIN "Orders" AS o  ON c.id = o."courierId"
WHERE o."inDelivery" = true 
GROUP BY c.login;