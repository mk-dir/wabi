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
    cur.execute("""create table sales (
	id INT,
	cust_id INT,
	inv_id INT,
	quantity INT,
	created_at DATE
        );
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (1, 1, 1, 51, '2019-06-22 11:22:29');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (2, 2, 2, 13, '2020-01-03 08:56:41');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (3, 3, 3, 53, '2019-11-21 12:53:32');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (4, 4, 4, 82, '2019-07-18 13:30:59');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (5, 5, 5, 65, '2020-01-24 12:25:09');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (6, 6, 6, 7, '2019-03-26 10:15:26');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (7, 7, 7, 77, '2019-04-19 11:15:30');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (8, 8, 8, 45, '2020-01-16 14:45:03');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (9, 9, 9, 49, '2020-01-10 09:38:39');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (10, 10, 10, 99, '2019-09-22 12:29:54');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (11, 11, 11, 73, '2019-10-04 08:31:42');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (12, 12, 12, 92, '2020-01-03 19:04:38');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (13, 13, 13, 75, '2019-10-15 03:41:28');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (14, 14, 14, 71, '2019-03-15 16:22:01');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (15, 15, 15, 54, '2019-12-07 18:28:43');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (16, 16, 16, 56, '2019-03-04 02:41:24');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (17, 17, 17, 82, '2019-05-24 22:19:48');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (18, 18, 18, 41, '2020-01-13 08:08:40');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (19, 19, 19, 62, '2020-01-15 08:26:14');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (20, 20, 20, 61, '2019-11-18 09:15:02');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (21, 21, 21, 82, '2019-03-29 17:25:07');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (22, 22, 22, 85, '2019-06-17 02:38:47');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (23, 23, 23, 93, '2019-08-07 10:48:30');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (24, 24, 24, 90, '2019-09-22 22:14:24');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (25, 25, 25, 4, '2019-12-25 20:16:27');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (26, 26, 26, 3, '2019-07-21 22:47:37');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (27, 27, 27, 93, '2019-08-14 17:54:43');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (28, 28, 28, 49, '2019-03-20 13:42:44');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (29, 29, 29, 19, '2019-09-01 17:52:27');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (30, 30, 30, 2, '2019-10-14 09:58:06');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (31, 31, 31, 20, '2019-12-05 20:53:34');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (32, 32, 32, 68, '2019-12-17 05:30:11');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (33, 33, 33, 80, '2019-06-07 11:42:00');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (34, 34, 34, 81, '2019-07-15 07:33:38');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (35, 35, 35, 15, '2019-10-30 07:17:48');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (36, 36, 36, 53, '2019-11-18 03:57:48');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (37, 37, 37, 3, '2019-12-03 13:43:02');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (38, 38, 38, 57, '2019-10-02 19:22:58');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (39, 39, 39, 60, '2019-03-12 12:30:58');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (40, 40, 40, 20, '2019-11-10 12:26:43');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (41, 41, 41, 10, '2019-08-27 01:07:57');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (42, 42, 42, 47, '2020-01-26 08:17:46');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (43, 43, 43, 49, '2019-08-30 15:12:48');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (44, 44, 44, 87, '2019-08-11 09:47:14');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (45, 45, 45, 26, '2019-02-28 21:49:39');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (46, 46, 46, 16, '2019-03-22 12:02:16');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (47, 47, 47, 22, '2019-07-29 10:50:29');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (48, 48, 48, 52, '2019-04-28 04:12:05');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (49, 49, 49, 38, '2019-05-12 08:06:54');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (50, 50, 50, 100, '2019-08-07 20:52:08');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (51, 51, 51, 95, '2019-08-20 22:33:02');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (52, 52, 52, 1, '2019-07-01 12:25:22');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (53, 53, 53, 29, '2019-04-12 13:47:38');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (54, 54, 54, 32, '2019-10-25 04:16:00');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (55, 55, 55, 1, '2019-07-28 08:46:39');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (56, 56, 56, 100, '2019-02-21 11:38:56');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (57, 57, 57, 100, '2019-02-22 09:02:49');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (58, 58, 58, 81, '2019-07-23 11:09:00');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (59, 59, 59, 80, '2019-09-20 04:37:43');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (60, 60, 60, 9, '2019-03-31 11:15:40');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (61, 61, 61, 14, '2020-01-06 05:20:20');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (62, 62, 62, 85, '2019-09-08 10:20:50');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (63, 63, 63, 92, '2019-10-29 11:55:59');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (64, 64, 64, 13, '2019-06-08 22:48:45');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (65, 65, 65, 13, '2019-07-04 16:45:16');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (66, 66, 66, 45, '2019-09-03 11:45:10');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (67, 67, 67, 77, '2019-06-28 23:04:55');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (68, 68, 68, 54, '2019-10-09 07:22:54');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (69, 69, 69, 12, '2019-11-06 03:50:42');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (70, 70, 70, 13, '2019-09-30 21:57:06');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (71, 71, 71, 79, '2019-06-17 08:43:31');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (72, 72, 72, 34, '2019-08-04 15:48:37');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (73, 73, 73, 45, '2019-03-08 15:37:04');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (74, 74, 74, 75, '2019-06-06 10:15:36');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (75, 75, 75, 87, '2020-01-06 12:42:37');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (76, 76, 76, 22, '2019-09-05 09:15:08');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (77, 77, 77, 86, '2020-01-03 05:36:18');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (78, 78, 78, 7, '2019-11-11 23:00:24');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (79, 79, 79, 57, '2019-05-19 17:29:28');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (80, 80, 80, 80, '2019-09-13 04:52:47');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (81, 81, 81, 70, '2019-06-20 05:19:23');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (82, 82, 82, 85, '2019-02-13 15:45:49');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (83, 83, 83, 31, '2019-05-07 02:16:54');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (84, 84, 84, 26, '2019-10-22 09:14:21');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (85, 85, 85, 17, '2019-12-09 17:40:02');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (86, 86, 86, 35, '2019-02-28 20:48:26');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (87, 87, 87, 29, '2019-08-11 15:27:41');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (88, 88, 88, 80, '2020-01-02 20:24:41');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (89, 89, 89, 33, '2019-02-14 06:30:46');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (90, 90, 90, 81, '2019-07-29 19:45:58');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (91, 91, 91, 32, '2019-06-26 03:59:44');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (92, 92, 92, 40, '2019-08-07 17:51:54');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (93, 93, 93, 76, '2020-01-15 04:10:39');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (94, 94, 94, 39, '2019-11-06 20:31:37');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (95, 95, 95, 83, '2019-06-13 18:52:07');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (96, 96, 96, 88, '2019-08-24 17:37:33');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (97, 97, 97, 40, '2019-08-29 18:20:56');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (98, 98, 98, 56, '2019-09-01 11:47:10');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (99, 99, 99, 13, '2019-06-10 17:54:12');
        insert into sales (id, cust_id, inv_id, quantity, created_at) values (100, 100, 100, 83, '2019-05-20 01:11:26');""")

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
    