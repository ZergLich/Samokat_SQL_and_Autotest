SELECT	id, 
	"courierId", 
	track, 
	"inDelivery", 
	cancelled, 
	finished,
	CASE	-- вычисление статуса заказа на основе значений полей
		-- inDelivery, cancelled и finished
	    WHEN cancelled = true
	    THEN -1
	    ELSE
	        CASE
		    WHEN "inDelivery" = false
		    THEN 0
		    ELSE
			CASE
			    WHEN finished = true
			    THEN 2
			    ELSE 1
			END
		END
	END
	AS Status

FROM "Orders";

-- ================================

-- the same query in one row: SELECT	id, "courierId", track, "inDelivery", cancelled, finished, CASE	WHEN cancelled = true THEN -1 ELSE CASE WHEN "inDelivery" = false THEN 0 ELSE CASE WHEN finished = true THEN 2 ELSE 1 END END END AS Status FROM "Orders";