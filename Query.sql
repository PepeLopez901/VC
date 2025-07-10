
-- para sacar un cocatenado de ids o strings de una tabla relacionada con otra tabla
DECLARE @TblTemporal TABLE(Id_ INT ,ids_ NVARCHAR(MAX),Txt VARCHAR(max))

	INSERT INTO @TblTemporal (Id_ ,ids_)
		SELECT DISTINCT T2.Id_, SUBSTRING
								 ((SELECT        ',' + CAST(T1.Id_ AS VARCHAR) AS [text()]
									 FROM            Tabla1 T1
									 WHERE        T1.Id_= T2.Id_
									 ORDER BY T1.Id_FOR XML PATH('')), 2, 1000) [Ids], SUBSTRING
								 ((SELECT        ',' + CAST(t3.Id_ AS VARCHAR) AS [text()]
									 FROM            Tabla1 T1 INNER JOIN
															 tabla3 t3 ON t3.Id_ = T1.Id_
									 WHERE        T1.Id_ = T2.Id_
									 ORDER BY T1.Id_ FOR XML PATH('')), 2, 1000) [Des]
		FROM Tabla2 T2

		SELECT * from @TblTemporal


