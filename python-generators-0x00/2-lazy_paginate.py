#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

#-------------------------------------------------------------
# Create a lazy load to parse data 
#-------------------------------------------------------------
def lazy_loading(page_size): 
    offset = 0 

    while True: 
        users = paginate_users(page_size, offset)

        if not users: 
            break 
        yield users

        offset += page_size 

for user in lazy_loading(page_size=10): 
    print(user)