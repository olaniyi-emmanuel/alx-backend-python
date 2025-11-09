#-------------------------------------------------------
# Batch processing Large Data
#-------------------------------------------------------
import seed

def stream_users_in_batches(batch_size, offset): 
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()

    while True:
        sql = f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}" 
        cursor.execute(sql)
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch 
        offset += len(batch)

        #cursor.close()
    #connection.close()

if __name__ == "__main__": 
    for batch in stream_users_in_batches(batch_size=1, offset=1):
        print(batch)


