import psycopg2

conn = psycopg2.connect('dbname=udacity user=postgres password=default123')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute('DROP TABLE IF EXISTS customer;')

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute('''
  CREATE TABLE customer (
    id serial PRIMARY KEY,
    fname VARCHAR NOT NULL,
    lname VARCHAR NOT NULL,
    Dept VARCHAR NOT NULL
  );
''')
cur.execute('''
  Insert into customer values(1, 'nikhil', 'gupta', 'Testing');
''')

cur.execute('Insert into customer values(%s, %s, %s, %s);',(2,'ram', 'kumar','Developer'))

cur.execute('Insert into customer values(%(id)s, %(fname)s, %(lname)s, %(dept)s);',
{
  'id':3,
  'fname':'hanuman',
  'lname': 'Bajranbali',
  'dept': 'Security'
})

sql = 'Insert into customer values(%(id)s, %(fname)s,%(lname)s, %(dept)s);'
data = {
  'id':4,
  'fname':'Sita',
  'lname': 'ram',
  'dept': 'Kingdom'
}
cur.execute(sql,data)

cur.execute('''
  Select * from customer;
''')

#result = cur.fetchall();

result1= cur.fetchone();
result2= cur.fetchmany(2);
result3=cur.fetchall();

print('fetchone ',result1)
print('fetchmany(2)',result2)
print('fetchall', result3)
# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()
