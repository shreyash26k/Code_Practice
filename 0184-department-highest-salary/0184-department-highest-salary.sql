SELECT 
    temp.Department, 
    temp.Employee, 
    temp.Salary 
FROM (
    SELECT 
        D.NAME AS Department,
        E.NAME AS Employee,
        E.SALARY AS Salary,
        DENSE_RANK() OVER(PARTITION BY D.ID ORDER BY E.SALARY DESC) AS RNK
    FROM EMPLOYEE E 
    JOIN DEPARTMENT D ON E.departmentId = D.ID
) temp
WHERE temp.RNK = 1;