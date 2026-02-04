-- Last updated: 2/4/2026, 12:16:14 PM
# Write your MySQL query statement below
SELECT a.firstName, a.lastName, b.city, b.state 
FROM Person a
LEFT JOIN Address b
ON a.personID = b.personID 