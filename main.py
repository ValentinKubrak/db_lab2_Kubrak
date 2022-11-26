import psycopg2

username = 'Valentin'
password = 'qwerty123'
database = 'LW2'
host = 'localhost'
port = '5432'

query_1 = '''
select trim(country), count(country) from player group by country
'''

query_2 = '''
select 'in "home" team' as "status", count(*) 
from team join player on team.team_id = player.team_id where team.country = player.country
union
select 'in foreign team', count(*) 
from team join player on team.team_id = player.team_id where team.country != player.country
'''

query_3 = '''
select trim(player_name), score from statistic join player on statistic.player_id = player.player_id
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    print("Database opened successfully")

    cur = conn.cursor()
    print('\nQuery 1:')
    cur.execute(query_1)
    for row in cur.fetchall():
        print(row)

    print('\nQuery 2:')
    cur.execute(query_2)
    for row in cur.fetchall():
        print(row)

    print('\nQuery 3:')
    cur.execute(query_3)
    for row in cur.fetchall():
        print(row)