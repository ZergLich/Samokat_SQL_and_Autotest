-- 1. убран вывод лишних полей
-- 2. упрощен порядок использования CASE

SELECT	track, 
	CASE	-- вычисление статуса заказа на основе значений полей
		-- inDelivery, cancelled и finished с расчетом на то, что не может быть взаимоисключающих состояний в этих полях
		WHEN finished = true
		THEN 2
	    	WHEN cancelled = true
	    	THEN -1
	    	WHEN "inDelivery" = true
		THEN 1
		ELSE 0
	END
	AS "SimpleStatus"

FROM "Orders";
