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
	quantity INT,
	created_at DATE
);
insert into stocks (id, inv_id, quantity, created_at) values (1, 1, 93, '21/10/2018');
insert into stocks (id, inv_id, quantity, created_at) values (2, 2, 52, '22/7/2009');
insert into stocks (id, inv_id, quantity, created_at) values (3, 3, 59, '16/9/2011');
insert into stocks (id, inv_id, quantity, created_at) values (4, 4, 24, '27/5/2011');
insert into stocks (id, inv_id, quantity, created_at) values (5, 5, 36, '20/10/2014');
insert into stocks (id, inv_id, quantity, created_at) values (6, 6, 42, '22/12/2012');
insert into stocks (id, inv_id, quantity, created_at) values (7, 7, 34, '29/9/2017');
insert into stocks (id, inv_id, quantity, created_at) values (8, 8, 60, '21/3/2016');
insert into stocks (id, inv_id, quantity, created_at) values (9, 9, 51, '1/9/2015');
insert into stocks (id, inv_id, quantity, created_at) values (10, 10, 3, '14/8/2012');
insert into stocks (id, inv_id, quantity, created_at) values (11, 11, 54, '22/9/2009');
insert into stocks (id, inv_id, quantity, created_at) values (12, 12, 36, '1/2/2012');
insert into stocks (id, inv_id, quantity, created_at) values (13, 13, 82, '7/12/2010');
insert into stocks (id, inv_id, quantity, created_at) values (14, 14, 9, '19/3/2009');
insert into stocks (id, inv_id, quantity, created_at) values (15, 15, 96, '15/6/2016');
insert into stocks (id, inv_id, quantity, created_at) values (16, 16, 28, '12/2/2018');
insert into stocks (id, inv_id, quantity, created_at) values (17, 17, 54, '14/7/2012');
insert into stocks (id, inv_id, quantity, created_at) values (18, 18, 81, '7/9/2009');
insert into stocks (id, inv_id, quantity, created_at) values (19, 19, 51, '23/2/2016');
insert into stocks (id, inv_id, quantity, created_at) values (20, 20, 77, '10/2/2012');
insert into stocks (id, inv_id, quantity, created_at) values (21, 21, 41, '26/5/2012');
insert into stocks (id, inv_id, quantity, created_at) values (22, 22, 7, '20/6/2013');
insert into stocks (id, inv_id, quantity, created_at) values (23, 23, 78, '23/12/2015');
insert into stocks (id, inv_id, quantity, created_at) values (24, 24, 12, '9/10/2010');
insert into stocks (id, inv_id, quantity, created_at) values (25, 25, 98, '21/5/2018');
insert into stocks (id, inv_id, quantity, created_at) values (26, 26, 29, '9/4/2017');
insert into stocks (id, inv_id, quantity, created_at) values (27, 27, 37, '3/2/2014');
insert into stocks (id, inv_id, quantity, created_at) values (28, 28, 7, '30/5/2014');
insert into stocks (id, inv_id, quantity, created_at) values (29, 29, 84, '14/6/2017');
insert into stocks (id, inv_id, quantity, created_at) values (30, 30, 33, '15/5/2011');
insert into stocks (id, inv_id, quantity, created_at) values (31, 31, 14, '20/12/2018');
insert into stocks (id, inv_id, quantity, created_at) values (32, 32, 57, '6/3/2011');
insert into stocks (id, inv_id, quantity, created_at) values (33, 33, 56, '16/10/2014');
insert into stocks (id, inv_id, quantity, created_at) values (34, 34, 58, '5/2/2017');
insert into stocks (id, inv_id, quantity, created_at) values (35, 35, 88, '15/8/2011');
insert into stocks (id, inv_id, quantity, created_at) values (36, 36, 75, '1/9/2013');
insert into stocks (id, inv_id, quantity, created_at) values (37, 37, 37, '14/11/2010');
insert into stocks (id, inv_id, quantity, created_at) values (38, 38, 24, '10/7/2011');
insert into stocks (id, inv_id, quantity, created_at) values (39, 39, 22, '30/10/2013');
insert into stocks (id, inv_id, quantity, created_at) values (40, 40, 51, '10/12/2014');
insert into stocks (id, inv_id, quantity, created_at) values (41, 41, 83, '24/12/2013');
insert into stocks (id, inv_id, quantity, created_at) values (42, 42, 23, '8/7/2013');
insert into stocks (id, inv_id, quantity, created_at) values (43, 43, 60, '16/2/2011');
insert into stocks (id, inv_id, quantity, created_at) values (44, 44, 86, '23/12/2011');
insert into stocks (id, inv_id, quantity, created_at) values (45, 45, 68, '11/5/2011');
insert into stocks (id, inv_id, quantity, created_at) values (46, 46, 99, '6/6/2018');
insert into stocks (id, inv_id, quantity, created_at) values (47, 47, 79, '26/6/2011');
insert into stocks (id, inv_id, quantity, created_at) values (48, 48, 20, '17/1/2012');
insert into stocks (id, inv_id, quantity, created_at) values (49, 49, 42, '1/7/2013');
insert into stocks (id, inv_id, quantity, created_at) values (50, 50, 48, '16/5/2014');
insert into stocks (id, inv_id, quantity, created_at) values (51, 51, 83, '1/6/2012');
insert into stocks (id, inv_id, quantity, created_at) values (52, 52, 10, '12/9/2015');
insert into stocks (id, inv_id, quantity, created_at) values (53, 53, 68, '14/11/2018');
insert into stocks (id, inv_id, quantity, created_at) values (54, 54, 39, '8/5/2012');
insert into stocks (id, inv_id, quantity, created_at) values (55, 55, 3, '25/3/2014');
insert into stocks (id, inv_id, quantity, created_at) values (56, 56, 11, '26/9/2011');
insert into stocks (id, inv_id, quantity, created_at) values (57, 57, 48, '22/5/2018');
insert into stocks (id, inv_id, quantity, created_at) values (58, 58, 91, '30/4/2013');
insert into stocks (id, inv_id, quantity, created_at) values (59, 59, 2, '22/9/2012');
insert into stocks (id, inv_id, quantity, created_at) values (60, 60, 26, '12/8/2011');
insert into stocks (id, inv_id, quantity, created_at) values (61, 61, 91, '28/8/2016');
insert into stocks (id, inv_id, quantity, created_at) values (62, 62, 89, '4/1/2012');
insert into stocks (id, inv_id, quantity, created_at) values (63, 63, 18, '19/2/2015');
insert into stocks (id, inv_id, quantity, created_at) values (64, 64, 73, '8/4/2013');
insert into stocks (id, inv_id, quantity, created_at) values (65, 65, 96, '22/12/2017');
insert into stocks (id, inv_id, quantity, created_at) values (66, 66, 34, '10/12/2010');
insert into stocks (id, inv_id, quantity, created_at) values (67, 67, 12, '29/3/2016');
insert into stocks (id, inv_id, quantity, created_at) values (68, 68, 36, '23/11/2017');
insert into stocks (id, inv_id, quantity, created_at) values (69, 69, 44, '30/10/2009');
insert into stocks (id, inv_id, quantity, created_at) values (70, 70, 27, '4/3/2013');
insert into stocks (id, inv_id, quantity, created_at) values (71, 71, 97, '21/8/2010');
insert into stocks (id, inv_id, quantity, created_at) values (72, 72, 64, '18/3/2009');
insert into stocks (id, inv_id, quantity, created_at) values (73, 73, 99, '16/1/2019');
insert into stocks (id, inv_id, quantity, created_at) values (74, 74, 94, '28/11/2016');
insert into stocks (id, inv_id, quantity, created_at) values (75, 75, 77, '10/9/2009');
insert into stocks (id, inv_id, quantity, created_at) values (76, 76, 83, '9/2/2019');
insert into stocks (id, inv_id, quantity, created_at) values (77, 77, 25, '17/2/2015');
insert into stocks (id, inv_id, quantity, created_at) values (78, 78, 86, '18/2/2017');
insert into stocks (id, inv_id, quantity, created_at) values (79, 79, 34, '16/5/2011');
insert into stocks (id, inv_id, quantity, created_at) values (80, 80, 94, '4/2/2014');
insert into stocks (id, inv_id, quantity, created_at) values (81, 81, 2, '5/9/2012');
insert into stocks (id, inv_id, quantity, created_at) values (82, 82, 18, '24/12/2017');
insert into stocks (id, inv_id, quantity, created_at) values (83, 83, 24, '1/3/2016');
insert into stocks (id, inv_id, quantity, created_at) values (84, 84, 91, '22/11/2013');
insert into stocks (id, inv_id, quantity, created_at) values (85, 85, 36, '24/10/2016');
insert into stocks (id, inv_id, quantity, created_at) values (86, 86, 31, '4/11/2013');
insert into stocks (id, inv_id, quantity, created_at) values (87, 87, 31, '26/4/2015');
insert into stocks (id, inv_id, quantity, created_at) values (88, 88, 7, '23/12/2009');
insert into stocks (id, inv_id, quantity, created_at) values (89, 89, 69, '23/4/2014');
insert into stocks (id, inv_id, quantity, created_at) values (90, 90, 7, '24/4/2010');
insert into stocks (id, inv_id, quantity, created_at) values (91, 91, 84, '27/6/2014');
insert into stocks (id, inv_id, quantity, created_at) values (92, 92, 91, '6/9/2015');
insert into stocks (id, inv_id, quantity, created_at) values (93, 93, 36, '22/9/2018');
insert into stocks (id, inv_id, quantity, created_at) values (94, 94, 91, '23/11/2011');
insert into stocks (id, inv_id, quantity, created_at) values (95, 95, 41, '14/1/2018');
insert into stocks (id, inv_id, quantity, created_at) values (96, 96, 65, '7/5/2017');
insert into stocks (id, inv_id, quantity, created_at) values (97, 97, 83, '9/6/2016');
insert into stocks (id, inv_id, quantity, created_at) values (98, 98, 9, '15/5/2010');
insert into stocks (id, inv_id, quantity, created_at) values (99, 99, 85, '28/10/2010');
insert into stocks (id, inv_id, quantity, created_at) values (100, 100, 99, '25/1/2015');""")

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
    