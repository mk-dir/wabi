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
insert into sales (id, cust_id, inv_id, quantity, created_at) values (1, 1, 1, 34, '2/5/2009');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (2, 2, 2, 11, '16/8/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (3, 3, 3, 40, '15/7/2013');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (4, 4, 4, 2, '14/6/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (5, 5, 5, 47, '22/7/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (6, 6, 6, 48, '10/7/2010');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (7, 7, 7, 69, '5/11/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (8, 8, 8, 79, '16/5/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (9, 9, 9, 21, '10/10/2011');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (10, 10, 10, 78, '2/3/2014');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (11, 11, 11, 41, '21/11/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (12, 12, 12, 16, '27/1/2013');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (13, 13, 13, 74, '4/5/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (14, 14, 14, 38, '27/7/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (15, 15, 15, 63, '14/12/2011');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (16, 16, 16, 54, '8/8/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (17, 17, 17, 50, '14/3/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (18, 18, 18, 7, '10/5/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (19, 19, 19, 69, '15/11/2010');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (20, 20, 20, 57, '5/7/2010');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (21, 21, 21, 17, '2/10/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (22, 22, 22, 33, '15/11/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (23, 23, 23, 80, '30/7/2013');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (24, 24, 24, 84, '29/4/2013');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (25, 25, 25, 71, '17/6/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (26, 26, 26, 96, '4/5/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (27, 27, 27, 8, '25/12/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (28, 28, 28, 86, '26/3/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (29, 29, 29, 49, '9/3/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (30, 30, 30, 27, '19/9/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (31, 31, 31, 45, '26/11/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (32, 32, 32, 71, '12/1/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (33, 33, 33, 61, '17/10/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (34, 34, 34, 53, '23/4/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (35, 35, 35, 46, '6/11/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (36, 36, 36, 52, '19/4/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (37, 37, 37, 76, '20/2/2010');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (38, 38, 38, 18, '20/7/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (39, 39, 39, 73, '16/3/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (40, 40, 40, 53, '21/6/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (41, 41, 41, 69, '15/3/2013');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (42, 42, 42, 50, '9/9/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (43, 43, 43, 65, '7/3/2013');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (44, 44, 44, 48, '17/3/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (45, 45, 45, 65, '7/3/2011');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (46, 46, 46, 84, '9/3/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (47, 47, 47, 44, '23/9/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (48, 48, 48, 29, '30/9/2014');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (49, 49, 49, 96, '31/10/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (50, 50, 50, 14, '26/6/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (51, 51, 51, 43, '6/1/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (52, 52, 52, 70, '13/1/2010');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (53, 53, 53, 75, '25/5/2009');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (54, 54, 54, 75, '20/8/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (55, 55, 55, 88, '10/10/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (56, 56, 56, 33, '25/4/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (57, 57, 57, 54, '21/5/2013');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (58, 58, 58, 86, '24/8/2014');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (59, 59, 59, 14, '22/6/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (60, 60, 60, 62, '5/1/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (61, 61, 61, 67, '17/1/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (62, 62, 62, 86, '16/6/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (63, 63, 63, 49, '30/6/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (64, 64, 64, 48, '24/6/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (65, 65, 65, 42, '11/3/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (66, 66, 66, 98, '6/9/2014');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (67, 67, 67, 61, '26/3/2010');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (68, 68, 68, 67, '23/9/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (69, 69, 69, 51, '17/7/2013');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (70, 70, 70, 93, '4/10/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (71, 71, 71, 20, '29/6/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (72, 72, 72, 46, '19/1/2019');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (73, 73, 73, 78, '2/1/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (74, 74, 74, 55, '16/4/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (75, 75, 75, 31, '11/3/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (76, 76, 76, 97, '11/7/2014');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (77, 77, 77, 38, '20/12/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (78, 78, 78, 61, '14/5/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (79, 79, 79, 99, '12/10/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (80, 80, 80, 62, '15/2/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (81, 81, 81, 64, '16/6/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (82, 82, 82, 96, '6/6/2010');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (83, 83, 83, 71, '6/11/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (84, 84, 84, 40, '14/1/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (85, 85, 85, 36, '4/7/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (86, 86, 86, 7, '1/12/2015');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (87, 87, 87, 36, '10/3/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (88, 88, 88, 94, '24/3/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (89, 89, 89, 22, '11/11/2011');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (90, 90, 90, 42, '19/11/2009');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (91, 91, 91, 56, '16/11/2017');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (92, 92, 92, 49, '7/4/2016');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (93, 93, 93, 39, '10/9/2011');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (94, 94, 94, 34, '17/5/2012');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (95, 95, 95, 4, '24/4/2013');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (96, 96, 96, 12, '3/6/2014');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (97, 97, 97, 14, '22/8/2014');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (98, 98, 98, 94, '21/6/2014');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (99, 99, 99, 8, '23/12/2018');
insert into sales (id, cust_id, inv_id, quantity, created_at) values (100, 100, 100, 24, '14/6/2016');""")

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
    