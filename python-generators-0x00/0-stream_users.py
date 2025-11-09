#--------------------------------------------------------------------
# Create a function to  stream data from the dtabase using generator
#--------------------------------------------------------------------
from itertools import islice
import seed 
def stream_users():
    connection = seed.connect_to_prodev() 
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user_data LIMIT 100;")
    rows =   cursor.fetchall()
    for _users in rows: 
        yield _users

for user in islice(stream_users(), 6):
    print(user)
