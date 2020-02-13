from flask import Flask, render_template, escape
import pygal
import psycopg2


app = Flask(__name__)
title='Robot'
posts=[
    {'Author':'Cullen',
'Title':'I am Legend',
'Date_posted':'21 April 2018'},
{'Author':'Nkiro',
'Title':'I am Legendess',
'Date_posted':'21 October 2018'}]

@app.route("/")

def helloworld():
    # # postgres://zrgirmyqlrnepr:80841ec233ebb6b65f7249a8c6bb7402649dbaf0c5e7415d3a449eef2c89c479@ec2-54-195-247-108.eu-west-1.compute.amazonaws.com:5432/d1eihvigupehq7
    # conn=psycopg2.connect("dbname='d1eihvigupehq7' user='zrgirmyqlrnepr' host='ec2-54-195-247-108.eu-west-1.compute.amazonaws.com' password='80841ec233ebb6b65f7249a8c6bb7402649dbaf0c5e7415d3a449eef2c89c479'")

    # cur=conn.cursor()
    # cur.execute("Enter SQL query HERe")

    # records = cur.fetchall()

    graph=pygal.Line()
    graph.title='Language Popularity'
    graph.x_labels=['2011','2012','2013','2014','2015','2016']

    graph.add('python',[15,31,89,200,356,900])
    graph.add('java',[15,45,76,80,91,95])
    graph.add('C++',[5,51,54,102,150,201])
    graph.add('All others',[5,15,21,55,92,105])

    graphics=pygal.Pie()
    graphics.title='Language Popularity'
    graphics.x_labels=['2011','2012','2013','2014','2015','2016']

    graphics.add('python',[15,31,89,200,356,900])
    graphics.add('java',[15,45,76,80,91,95])
    graphics.add('C++',[5,51,54,102,150,201])
    graphics.add('All others',[5,15,21,55,92,105])

    graphics_data=graphics.render_data_uri()
    graph_data=graph.render_data_uri()
    return render_template('graph.html',graph_data=graph_data,graphics_data=graphics_data,title='Redsan',intro='Introduction',about='Let\'s start')

# Route to home

@app.route("/index")
def index():

    return render_template('index.html',name='About Page',site='Olegesaile')
#add Route

@app.route('/projects/<test>')
def projects(test):
    return render_template('test.html',posts=posts,title=test)

#routeledge

@app.route('/push')
def profile():
    conn=psycopg2.connect("dbname=d1eihvigupehq7 user=zrgirmyqlrnepr host=ec2-54-195-247-108.eu-west-1.compute.amazonaws.com password=80841ec233ebb6b65f7249a8c6bb7402649dbaf0c5e7415d3a449eef2c89c479 ")

    
# Open a cursor to perform database operations
    cur = conn.cursor()
    
    #create Table Script
    cur.execute("""create table inventory (
	id INT,
	cust_id INT,
	inv_id INT,
	quantity INT,
	created_at DATE
    );
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (1, 1, 1, 15, '2019-05-22 01:25:54');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (2, 2, 2, 50, '2019-10-02 12:04:59');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (3, 3, 3, 29, '2019-06-01 11:00:15');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (4, 4, 4, 74, '2019-10-13 15:44:31');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (5, 5, 5, 90, '2019-08-21 18:28:04');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (6, 6, 6, 75, '2019-03-19 14:39:22');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (7, 7, 7, 99, '2019-11-16 23:56:29');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (8, 8, 8, 13, '2019-04-13 03:04:09');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (9, 9, 9, 34, '2019-09-21 07:35:30');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (10, 10, 10, 37, '2019-09-17 02:16:37');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (11, 11, 11, 94, '2019-11-30 18:00:43');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (12, 12, 12, 6, '2019-10-26 14:53:45');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (13, 13, 13, 10, '2019-05-05 04:30:04');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (14, 14, 14, 60, '2019-07-27 12:53:26');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (15, 15, 15, 15, '2019-12-04 01:11:01');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (16, 16, 16, 90, '2019-07-13 09:15:36');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (17, 17, 17, 25, '2019-08-22 13:45:51');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (18, 18, 18, 11, '2019-05-12 23:11:45');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (19, 19, 19, 90, '2019-07-02 12:37:30');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (20, 20, 20, 20, '2019-09-13 12:40:15');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (21, 21, 21, 55, '2019-06-22 15:18:20');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (22, 22, 22, 58, '2019-05-06 03:32:24');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (23, 23, 23, 40, '2019-11-06 13:25:49');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (24, 24, 24, 11, '2019-10-03 06:15:41');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (25, 25, 25, 71, '2019-12-28 05:03:42');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (26, 26, 26, 91, '2019-09-07 06:25:53');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (27, 27, 27, 37, '2019-07-01 05:52:00');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (28, 28, 28, 44, '2019-09-28 04:53:06');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (29, 29, 29, 39, '2019-07-20 00:41:50');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (30, 30, 30, 51, '2019-09-02 04:02:30');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (31, 31, 31, 37, '2019-02-21 00:13:27');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (32, 32, 32, 87, '2019-11-30 08:30:17');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (33, 33, 33, 33, '2019-09-06 22:25:43');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (34, 34, 34, 17, '2019-05-22 06:15:16');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (35, 35, 35, 75, '2019-08-29 01:35:11');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (36, 36, 36, 58, '2019-08-19 09:36:33');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (37, 37, 37, 40, '2019-07-02 23:00:25');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (38, 38, 38, 88, '2019-10-15 18:01:15');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (39, 39, 39, 20, '2019-11-26 14:15:33');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (40, 40, 40, 11, '2020-01-15 16:03:15');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (41, 41, 41, 44, '2019-07-23 12:44:38');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (42, 42, 42, 78, '2019-11-07 03:58:34');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (43, 43, 43, 74, '2019-06-07 19:22:44');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (44, 44, 44, 3, '2019-09-18 01:28:46');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (45, 45, 45, 79, '2019-04-27 22:43:12');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (46, 46, 46, 95, '2019-09-26 15:55:06');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (47, 47, 47, 40, '2019-11-25 21:08:32');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (48, 48, 48, 22, '2019-05-11 14:40:57');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (49, 49, 49, 19, '2019-06-15 20:43:20');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (50, 50, 50, 24, '2019-05-28 04:25:10');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (51, 51, 51, 9, '2019-08-28 17:17:18');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (52, 52, 52, 70, '2019-07-09 14:54:33');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (53, 53, 53, 60, '2019-11-26 05:35:48');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (54, 54, 54, 67, '2019-12-11 10:32:04');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (55, 55, 55, 1, '2019-03-15 15:31:30');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (56, 56, 56, 57, '2019-07-28 11:24:35');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (57, 57, 57, 9, '2019-05-11 04:43:57');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (58, 58, 58, 93, '2019-03-24 07:17:47');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (59, 59, 59, 60, '2019-05-10 08:06:57');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (60, 60, 60, 72, '2019-02-25 04:07:57');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (61, 61, 61, 11, '2019-10-26 21:47:50');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (62, 62, 62, 61, '2020-01-08 05:54:38');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (63, 63, 63, 3, '2019-09-23 09:54:22');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (64, 64, 64, 70, '2019-07-23 08:26:20');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (65, 65, 65, 57, '2019-06-10 07:03:09');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (66, 66, 66, 95, '2019-06-17 10:02:47');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (67, 67, 67, 39, '2019-05-13 02:07:07');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (68, 68, 68, 97, '2019-12-06 18:39:25');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (69, 69, 69, 71, '2019-12-18 12:51:41');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (70, 70, 70, 78, '2020-01-10 01:39:36');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (71, 71, 71, 68, '2019-09-19 00:14:37');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (72, 72, 72, 22, '2019-07-16 23:32:11');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (73, 73, 73, 9, '2019-08-13 22:01:27');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (74, 74, 74, 20, '2020-02-10 13:45:09');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (75, 75, 75, 68, '2019-07-08 22:43:23');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (76, 76, 76, 41, '2019-10-05 13:18:43');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (77, 77, 77, 68, '2020-01-16 20:30:31');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (78, 78, 78, 58, '2019-12-03 13:42:19');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (79, 79, 79, 26, '2019-10-08 17:51:09');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (80, 80, 80, 48, '2019-05-01 04:06:00');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (81, 81, 81, 54, '2019-11-12 20:32:46');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (82, 82, 82, 76, '2019-05-19 12:05:22');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (83, 83, 83, 88, '2019-02-19 17:36:08');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (84, 84, 84, 97, '2019-09-14 01:29:59');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (85, 85, 85, 7, '2019-05-20 08:26:08');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (86, 86, 86, 97, '2019-08-11 04:19:12');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (87, 87, 87, 63, '2019-03-08 14:34:47');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (88, 88, 88, 58, '2019-08-06 10:40:13');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (89, 89, 89, 43, '2019-12-01 13:32:59');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (90, 90, 90, 23, '2019-11-17 15:35:20');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (91, 91, 91, 68, '2019-12-26 15:58:57');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (92, 92, 92, 30, '2019-08-20 11:04:11');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (93, 93, 93, 41, '2019-12-18 05:17:26');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (94, 94, 94, 53, '2019-05-21 08:27:59');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (95, 95, 95, 30, '2019-10-15 04:50:39');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (96, 96, 96, 96, '2019-04-06 18:34:12');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (97, 97, 97, 83, '2019-06-03 07:20:01');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (98, 98, 98, 38, '2019-04-04 23:32:31');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (99, 99, 99, 32, '2019-02-20 22:43:19');
    insert into inventory (id, cust_id, inv_id, quantity, created_at) values (100, 100, 100, 14, '2019-03-24 23:00:44');""")

    conn.commit()

    #close connection
    cur.close()

    conn.close()

    

    return 'Hello World'



@app.route('/blog')
def blog():
    return render_template('test.html',posts=posts,title='Eureka')


@app.route('/new')
def new():
    return render_template('new.html',fetuccine='recursive',indigo='purple',title='new')
    