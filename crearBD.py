import MySQLdb

conn = MySQLdb.connect(host="your_host", user="your_user", passwd="your_pass", db="your_db_name")

def crearBDyTablas():
    conn.text_factory = str    
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Subscriber (Mail varchar(32) PRIMARY KEY);')
    conn.commit()


crearBDyTablas()


