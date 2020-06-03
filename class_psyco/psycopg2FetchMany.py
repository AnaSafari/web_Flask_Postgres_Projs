import psycopg2

conn = psycopg2.connect('dbname=foo user=Anahita')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS price;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE price (
    id INTEGER PRIMARY KEY,
    isExpensive BOOLEAN NOT NULL DEFAULT False 
  );
""")

# add first row
cur.execute('INSERT INTO price (id, isExpensive)' +
'VALUES (%(id)s, %(isExpensive)s);',{
	'id':4,
	'isExpensive':False
})

#add second row
cur.execute("INSERT INTO price (id, isExpensive) VALUES(%s, %s);" ,(5, True))


#add third row
data = {
	'id':6,
	'isExpensive':False
}

SQL = 'INSERT INTO price (id, isExpensive) VALUES (%(id)s, %(isExpensive)s);'

cur.execute(SQL, data)

cur.execute('SELECT * FROM price')
# fetch the results
result1 = cur.fetchmany(2)
print('fetchFirst2',result1)

result2 = cur.fetchmany(1)
print('fetchrest', result2)

result3 = cur.fetchmany(1)
print('fetchfirstOneAgain', result3)

# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()

