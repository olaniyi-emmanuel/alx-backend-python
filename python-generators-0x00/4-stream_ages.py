seed = __import__('seed')

def age_of_users():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT age FROM user_data")
    rows = cursor.fetchall()
    connection.close()
    for row in rows: 
        yield  row['age']
    #print(next(rows))


def stream_user_ages():
    sum_of_age = 0 
    count = 0 
    
    for age in age_of_users():
        sum_of_age += age 
        count += 1 
        
        if not age: 
            break 
    average_age = sum_of_age / count 
    return print(f"Average age of users: {average_age}")

stream_user_ages() 
