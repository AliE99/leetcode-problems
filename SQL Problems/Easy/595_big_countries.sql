-- Write your PostgreSQL query statement below
select name, population, area
from World
where area >= 3_000_000 or population >= 25_000_000;