# from flask import Flask, request, make_response, render_template
# import click
# from flask import current_app, g
# from flask.cli import with_appcontext

# import psycopg2
#
# try:
#     conn = psycopg2.connect("dbname='todo_app'")
#     print("We Done it!")
# except:
#     print("You have an error")
#
#
# cur = conn.cursor()
# cur.execute("SELECT *")
# zach = cur.fetchall()
# print(zach)
# conn.close()

# with open('index.html', 'a') as post:
#     cur.copy_expert(outputquery, post)
