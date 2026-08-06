/* Write your PL/SQL query statement below */
select score,Dense_Rank() over(order by score Desc)As "rank" 
from Scores;