SELECT t2.unique_id, t1.name FROM Employees AS t1 
LEFT JOIN EmployeeUNI AS T2
ON t1.ID = T2.unique_id
