-- Стовпчикова діаграма - загальна кількість гравців по країнам
select trim(country), count(country) from player group by country

-- Кругова діаграма - співвідношення гравця до команди своєї країни чи іноземної
select 'in "home" team' as "status", count(*) 
from team join player on team.team_id = player.team_id where team.country = player.country
union
select 'in foreign team', count(*) 
from team join player on team.team_id = player.team_id where team.country != player.country

-- Графік залежності - співвідношення гравця та балів
select trim(player_name), score from statistic join player on statistic.player_id = player.player_id