import psycopg2

conn = psycopg2.connect('postgres://localhost/test')


def copy_from_file(cursor, filename, tablename):
        with open(filename, 'r') as f:
          columns = next(f).strip()  # header row          
          #cursor.copy_from(f, tablename, sep=',', null='')
          cursor.copy_expert(f"""COPY {tablename}({columns}) from STDIN with (FORMAT CSV)""", f)
            

with conn:
    with conn.cursor() as curs:
        curs.execute('select * from candidates')
        for record in curs:
          print(record)
        
        copy_from_file(curs, 'something.csv', 'candidates')

        curs.execute('select * from candidates')
        for record in curs:
          print(record)


# leaving contexts doesn't close the connection
conn.close()