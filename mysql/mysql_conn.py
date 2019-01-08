import pymysql


conn = pymysql.connect(host='localhost', port=3306)

cursor = conn.cursor()

result = cursor.execute('use test')

# create_table = "create table student(" \
#                "id int(11) primary key auto_increment," \
#                "name varchar(20) not null default''," \
#                "gender char(1) not null default''," \
#                "reg_date datetime);"
# result = cursor.execute(create_table)

data = [
    ('N1','M','2018-01-08'),
    ('N2','M','2018-01-07'),
    ('N3','M','2018-01-06'),
]

cursor.executemany('INSERT INTO student(name, gender, reg_date) values(%s,%s,%s)', data)

# for db in (cursor.fetchall()):
#
#     print(db)
#     #print(type(db)) #   <class 'tuple'>