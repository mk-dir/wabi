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

@app.route("/graph")

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

@app.route('/user/<username>')
def profile(username):
    return '{}\'s Profile'.format(escape(username))



@app.route('/blog')
def blog():
    return render_template('test.html',posts=posts,title='Eureka')


@app.route('/new')
def new():
    return render_template('new.html',fetuccine='recursive',indigo='purple',title='new')
    