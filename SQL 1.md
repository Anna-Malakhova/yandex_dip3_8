﻿SELECT c.login, 

COUNT(o."inDelivery") AS Orders_count

FROM "Couriers" AS c

INNER JOIN "Orders" AS o ON c.id = o."courierId"

WHERE o."inDelivery" = true

GROUP BY c.login;