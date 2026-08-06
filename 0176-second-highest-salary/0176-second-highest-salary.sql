/* Write your PL/SQL query statement below */
select Max(salary) as SecondHighestSalary
from (select salary,Dense_Rank() over (order by salary desc) As rnk from Employee )
where rnk=2;