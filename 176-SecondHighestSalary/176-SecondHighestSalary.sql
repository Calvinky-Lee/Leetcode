-- Last updated: 2/4/2026, 12:16:12 PM
# Write your MySQL query statement below
SELECT(SELECT DISTINCT salary FROM employee 
ORDER by salary desc
LIMIT 1 OFFSET 1) AS SecondHighestSalary

