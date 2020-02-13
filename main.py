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
    cur.execute("""create table stocks (
	id INT,
	inv_id INT,
	created_at DATE,
	quantity INT
    );
    insert into stocks (id, inv_id, created_at, quantity) values (1, 1, '2019-10-22 23:34:22', 43);
    insert into stocks (id, inv_id, created_at, quantity) values (2, 2, '2019-04-13 20:57:56', 49);
    insert into stocks (id, inv_id, created_at, quantity) values (3, 3, '2019-03-11 08:15:33', 58);
    insert into stocks (id, inv_id, created_at, quantity) values (4, 4, '2019-06-11 09:43:39', 66);
    insert into stocks (id, inv_id, created_at, quantity) values (5, 5, '2019-12-08 13:28:37', 72);
    insert into stocks (id, inv_id, created_at, quantity) values (6, 6, '2019-07-21 22:44:52', 14);
    insert into stocks (id, inv_id, created_at, quantity) values (7, 7, '2019-04-24 00:14:48', 72);
    insert into stocks (id, inv_id, created_at, quantity) values (8, 8, '2019-10-13 20:58:28', 51);
    insert into stocks (id, inv_id, created_at, quantity) values (9, 9, '2020-02-02 06:53:14', 68);
    insert into stocks (id, inv_id, created_at, quantity) values (10, 10, '2019-09-11 13:27:47', 34);
    insert into stocks (id, inv_id, created_at, quantity) values (11, 11, '2019-10-12 07:19:28', 38);
    insert into stocks (id, inv_id, created_at, quantity) values (12, 12, '2019-06-22 07:01:48', 30);
    insert into stocks (id, inv_id, created_at, quantity) values (13, 13, '2019-02-23 22:56:27', 15);
    insert into stocks (id, inv_id, created_at, quantity) values (14, 14, '2019-10-21 13:46:34', 6);
    insert into stocks (id, inv_id, created_at, quantity) values (15, 15, '2019-03-21 12:51:39', 62);
    insert into stocks (id, inv_id, created_at, quantity) values (16, 16, '2019-08-02 10:57:27', 36);
    insert into stocks (id, inv_id, created_at, quantity) values (17, 17, '2019-11-22 07:24:31', 93);
    insert into stocks (id, inv_id, created_at, quantity) values (18, 18, '2019-11-20 11:49:17', 71);
    insert into stocks (id, inv_id, created_at, quantity) values (19, 19, '2019-08-31 22:45:25', 76);
    insert into stocks (id, inv_id, created_at, quantity) values (20, 20, '2020-01-01 13:09:54', 18);
    insert into stocks (id, inv_id, created_at, quantity) values (21, 21, '2019-11-26 02:05:40', 17);
    insert into stocks (id, inv_id, created_at, quantity) values (22, 22, '2019-06-12 12:01:47', 23);
    insert into stocks (id, inv_id, created_at, quantity) values (23, 23, '2019-03-02 12:18:46', 73);
    insert into stocks (id, inv_id, created_at, quantity) values (24, 24, '2019-10-20 17:03:59', 93);
    insert into stocks (id, inv_id, created_at, quantity) values (25, 25, '2019-06-25 05:07:23', 98);
    insert into stocks (id, inv_id, created_at, quantity) values (26, 26, '2019-04-06 01:41:02', 37);
    insert into stocks (id, inv_id, created_at, quantity) values (27, 27, '2019-02-16 04:56:02', 6);
    insert into stocks (id, inv_id, created_at, quantity) values (28, 28, '2019-10-02 02:07:32', 77);
    insert into stocks (id, inv_id, created_at, quantity) values (29, 29, '2019-09-10 08:02:28', 5);
    insert into stocks (id, inv_id, created_at, quantity) values (30, 30, '2019-07-04 11:07:21', 31);
    insert into stocks (id, inv_id, created_at, quantity) values (31, 31, '2019-10-20 00:19:07', 56);
    insert into stocks (id, inv_id, created_at, quantity) values (32, 32, '2019-09-02 18:56:18', 80);
    insert into stocks (id, inv_id, created_at, quantity) values (33, 33, '2019-09-06 21:13:14', 16);
    insert into stocks (id, inv_id, created_at, quantity) values (34, 34, '2019-04-01 22:38:14', 4);
    insert into stocks (id, inv_id, created_at, quantity) values (35, 35, '2019-03-09 22:59:55', 47);
    insert into stocks (id, inv_id, created_at, quantity) values (36, 36, '2019-05-17 02:45:15', 37);
    insert into stocks (id, inv_id, created_at, quantity) values (37, 37, '2019-06-04 07:01:43', 56);
    insert into stocks (id, inv_id, created_at, quantity) values (38, 38, '2019-08-09 02:32:21', 12);
    insert into stocks (id, inv_id, created_at, quantity) values (39, 39, '2019-05-15 17:12:12', 7);
    insert into stocks (id, inv_id, created_at, quantity) values (40, 40, '2019-06-06 12:52:01', 28);
    insert into stocks (id, inv_id, created_at, quantity) values (41, 41, '2019-07-24 04:29:19', 47);
    insert into stocks (id, inv_id, created_at, quantity) values (42, 42, '2019-09-02 00:12:31', 46);
    insert into stocks (id, inv_id, created_at, quantity) values (43, 43, '2019-08-08 00:46:36', 28);
    insert into stocks (id, inv_id, created_at, quantity) values (44, 44, '2020-02-02 19:45:39', 24);
    insert into stocks (id, inv_id, created_at, quantity) values (45, 45, '2019-07-16 03:56:39', 97);
    insert into stocks (id, inv_id, created_at, quantity) values (46, 46, '2020-02-04 13:32:24', 9);
    insert into stocks (id, inv_id, created_at, quantity) values (47, 47, '2019-05-24 10:31:31', 72);
    insert into stocks (id, inv_id, created_at, quantity) values (48, 48, '2019-06-09 07:01:43', 75);
    insert into stocks (id, inv_id, created_at, quantity) values (49, 49, '2019-10-18 16:18:40', 91);
    insert into stocks (id, inv_id, created_at, quantity) values (50, 50, '2019-12-26 09:13:19', 61);
    insert into stocks (id, inv_id, created_at, quantity) values (51, 51, '2019-03-19 08:19:05', 81);
    insert into stocks (id, inv_id, created_at, quantity) values (52, 52, '2019-06-15 23:14:54', 46);
    insert into stocks (id, inv_id, created_at, quantity) values (53, 53, '2019-11-26 15:33:42', 73);
    insert into stocks (id, inv_id, created_at, quantity) values (54, 54, '2019-03-15 08:34:31', 32);
    insert into stocks (id, inv_id, created_at, quantity) values (55, 55, '2019-09-20 11:02:34', 67);
    insert into stocks (id, inv_id, created_at, quantity) values (56, 56, '2019-03-26 00:57:31', 84);
    insert into stocks (id, inv_id, created_at, quantity) values (57, 57, '2019-06-10 17:20:07', 92);
    insert into stocks (id, inv_id, created_at, quantity) values (58, 58, '2019-03-29 17:05:29', 33);
    insert into stocks (id, inv_id, created_at, quantity) values (59, 59, '2019-04-26 02:21:43', 57);
    insert into stocks (id, inv_id, created_at, quantity) values (60, 60, '2019-06-24 09:16:22', 64);
    insert into stocks (id, inv_id, created_at, quantity) values (61, 61, '2019-10-08 02:42:54', 42);
    insert into stocks (id, inv_id, created_at, quantity) values (62, 62, '2019-09-10 04:30:59', 72);
    insert into stocks (id, inv_id, created_at, quantity) values (63, 63, '2019-05-14 17:47:51', 75);
    insert into stocks (id, inv_id, created_at, quantity) values (64, 64, '2020-02-07 07:59:22', 1);
    insert into stocks (id, inv_id, created_at, quantity) values (65, 65, '2019-06-27 05:53:57', 44);
    insert into stocks (id, inv_id, created_at, quantity) values (66, 66, '2019-12-03 17:24:48', 98);
    insert into stocks (id, inv_id, created_at, quantity) values (67, 67, '2019-03-08 03:18:02', 31);
    insert into stocks (id, inv_id, created_at, quantity) values (68, 68, '2019-11-20 06:10:24', 44);
    insert into stocks (id, inv_id, created_at, quantity) values (69, 69, '2019-04-14 17:48:13', 40);
    insert into stocks (id, inv_id, created_at, quantity) values (70, 70, '2020-01-07 04:55:35', 20);
    insert into stocks (id, inv_id, created_at, quantity) values (71, 71, '2019-12-08 00:17:46', 48);
    insert into stocks (id, inv_id, created_at, quantity) values (72, 72, '2019-12-22 03:36:59', 91);
    insert into stocks (id, inv_id, created_at, quantity) values (73, 73, '2019-08-07 16:27:47', 10);
    insert into stocks (id, inv_id, created_at, quantity) values (74, 74, '2019-08-05 10:58:34', 86);
    insert into stocks (id, inv_id, created_at, quantity) values (75, 75, '2019-03-30 20:07:01', 47);
    insert into stocks (id, inv_id, created_at, quantity) values (76, 76, '2019-08-14 15:34:50', 25);
    insert into stocks (id, inv_id, created_at, quantity) values (77, 77, '2020-02-07 11:45:47', 43);
    insert into stocks (id, inv_id, created_at, quantity) values (78, 78, '2019-07-10 21:28:03', 25);
    insert into stocks (id, inv_id, created_at, quantity) values (79, 79, '2019-12-20 07:03:12', 55);
    insert into stocks (id, inv_id, created_at, quantity) values (80, 80, '2019-05-16 05:47:53', 11);
    insert into stocks (id, inv_id, created_at, quantity) values (81, 81, '2019-12-20 00:17:02', 84);
    insert into stocks (id, inv_id, created_at, quantity) values (82, 82, '2019-08-15 14:41:49', 20);
    insert into stocks (id, inv_id, created_at, quantity) values (83, 83, '2020-01-10 06:47:34', 79);
    insert into stocks (id, inv_id, created_at, quantity) values (84, 84, '2020-01-28 08:09:33', 48);
    insert into stocks (id, inv_id, created_at, quantity) values (85, 85, '2019-04-11 02:03:53', 3);
    insert into stocks (id, inv_id, created_at, quantity) values (86, 86, '2019-05-01 13:44:34', 87);
    insert into stocks (id, inv_id, created_at, quantity) values (87, 87, '2020-02-02 13:03:59', 58);
    insert into stocks (id, inv_id, created_at, quantity) values (88, 88, '2019-04-27 03:49:38', 31);
    insert into stocks (id, inv_id, created_at, quantity) values (89, 89, '2020-02-11 14:45:27', 29);
    insert into stocks (id, inv_id, created_at, quantity) values (90, 90, '2019-06-06 14:47:36', 92);
    insert into stocks (id, inv_id, created_at, quantity) values (91, 91, '2019-08-21 15:05:59', 21);
    insert into stocks (id, inv_id, created_at, quantity) values (92, 92, '2019-11-04 16:45:31', 4);
    insert into stocks (id, inv_id, created_at, quantity) values (93, 93, '2019-04-16 23:13:20', 16);
    insert into stocks (id, inv_id, created_at, quantity) values (94, 94, '2019-11-25 20:08:06', 94);
    insert into stocks (id, inv_id, created_at, quantity) values (95, 95, '2020-01-16 12:40:50', 74);
    insert into stocks (id, inv_id, created_at, quantity) values (96, 96, '2019-04-25 10:15:49', 5);
    insert into stocks (id, inv_id, created_at, quantity) values (97, 97, '2020-02-02 15:07:18', 98);
    insert into stocks (id, inv_id, created_at, quantity) values (98, 98, '2019-03-04 20:33:50', 12);
    insert into stocks (id, inv_id, created_at, quantity) values (99, 99, '2019-04-12 12:24:36', 3);
    insert into stocks (id, inv_id, created_at, quantity) values (100, 100, '2020-01-18 19:37:56', 48);""")

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
    