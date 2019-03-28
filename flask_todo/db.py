# import psycopg2
# from psycopg2 import Error
#
# def first():
#     try:
#         conn = psycopg2.connect(database = "todo_app")
#         cur = connection.cursor()
#         create_table_query = '''CREATE TABLE todos
#             (created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#             todo           TEXT    NOT NULL,
#             completed         BOOLEAN NOT NULL); '''
#         cur.execute(create_table_query)
#         conn.commit()
#         print("Table was created")
#     except (Exception, psycopg2.DatabaseError) as error :
#         print ("Don't do that", error)
#     finally:
#         if(connection):
#             cur.close()
#             conn.close()
#             print("Connection is closed")
