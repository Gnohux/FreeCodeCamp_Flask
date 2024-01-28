from sqlalchemy import create_engine, text
# import sqlite3

#con = sqlite3.connect('database.db')
#cur = con.cursor()
#sql = "CREATE TABLE jobs(id INTEGER PRIMARY KEY,title TEXT NOT NULL,company TEXT NOT NULL,location TEXT,salary INTEGER)"
#cur.execute(sql)
#sql = "INSERT INTO jobs(title,company,location,salary) VALUES('Data Analyst','Google','Mountain View',150000)"
#sql = "INSERT INTO jobs(title,company,location,salary) VALUES('Data Scientist','Meta','Remote',130000)"
# sql = "SELECT * FROM jobs"
#cur.execute(sql)
# table = cur.fetchall()
# print(table)
#con.commit()
#con.close()

# db_connection_string = os.environ['DB_CONNECTION_STRING']
#engine = create_engine('mysql+pymysql://username:password@host:3306/database?charst=utf8mb4')
engine = create_engine('sqlite:///database.db')

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = []
    for row in result.all():
      result_dicts.append(row._asdict())
    return result_dicts