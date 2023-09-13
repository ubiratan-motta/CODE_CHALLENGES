SELECT t2.unique_id, t1.name FROM Employees AS t1 
LEFT JOIN EmployeeUNI AS T2
ON t1.id = T2.id
