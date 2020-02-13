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
	name VARCHAR(50),
	type VARCHAR(10),
	bp INT,
	sp INT
    );
    insert into inventory (id, name, type, bp, sp) values (1, 'Saskatoon Berries - Frozen', 'fruits', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (2, 'Pepper - Red Bell', 'vegetables', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (3, 'Ham - Procutinni', 'vegetables', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (4, 'Pasta - Fusili, Dry', 'cereals', 85, 106.25);
    insert into inventory (id, name, type, bp, sp) values (5, 'Wine - Hardys Bankside Shiraz', 'fruits', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (6, 'Juice - Lagoon Mango', 'vegetables', 11, 13.75);
    insert into inventory (id, name, type, bp, sp) values (7, 'Marjoram - Dried, Rubbed', 'vegetables', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (8, 'Bread - White Mini Epi', 'fruits', 25, 31.25);
    insert into inventory (id, name, type, bp, sp) values (9, 'Quinoa', 'vegetables', 4, 5);
    insert into inventory (id, name, type, bp, sp) values (10, 'Pepper - Chipotle, Canned', 'fruits', 10, 12.5);
    insert into inventory (id, name, type, bp, sp) values (11, 'Energy Drink - Franks Pineapple', 'cereals', 33, 41.25);
    insert into inventory (id, name, type, bp, sp) values (12, 'Tuna - Sushi Grade', 'cereals', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (13, 'Nectarines', 'fruits', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (14, 'Rum - White, Gg White', 'cereals', 47, 58.75);
    insert into inventory (id, name, type, bp, sp) values (15, 'Sping Loaded Cup Dispenser', 'vegetables', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (16, 'Cheese - Stilton', 'vegetables', 43, 53.75);
    insert into inventory (id, name, type, bp, sp) values (17, 'Sardines', 'vegetables', 97, 121.25);
    insert into inventory (id, name, type, bp, sp) values (18, 'Shrimp - Black Tiger 26/30', 'vegetables', 17, 21.25);
    insert into inventory (id, name, type, bp, sp) values (19, 'Lettuce - Lambs Mash', 'cereals', 48, 60);
    insert into inventory (id, name, type, bp, sp) values (20, 'Crackers - Melba Toast', 'cereals', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (21, 'Flower - Commercial Spider', 'fruits', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (22, 'Clementine', 'cereals', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (23, 'Bread - White, Unsliced', 'fruits', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (24, 'Squid - U 5', 'fruits', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (25, 'Wine - White, Cooking', 'vegetables', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (26, 'Juice - Pineapple, 341 Ml', 'vegetables', 7, 8.75);
    insert into inventory (id, name, type, bp, sp) values (27, 'Pear - Prickly', 'vegetables', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (28, 'Pasta - Lasagna Noodle, Frozen', 'fruits', 82, 102.5);
    insert into inventory (id, name, type, bp, sp) values (29, 'Sorrel - Fresh', 'fruits', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (30, 'Steampan - Lid For Half Size', 'fruits', 83, 103.75);
    insert into inventory (id, name, type, bp, sp) values (31, 'Hot Chocolate - Individual', 'cereals', 84, 105);
    insert into inventory (id, name, type, bp, sp) values (32, 'Wiberg Super Cure', 'fruits', 25, 31.25);
    insert into inventory (id, name, type, bp, sp) values (33, 'Muffin - Mix - Strawberry Rhubarb', 'fruits', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (34, 'Syrup - Monin - Passion Fruit', 'fruits', 23, 28.75);
    insert into inventory (id, name, type, bp, sp) values (35, 'Flour - Masa De Harina Mexican', 'vegetables', 41, 51.25);
    insert into inventory (id, name, type, bp, sp) values (36, 'Beans - Soya Bean', 'fruits', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (37, 'Wine - Chablis J Moreau Et Fils', 'cereals', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (38, 'Kaffir Lime Leaves', 'vegetables', 79, 98.75);
    insert into inventory (id, name, type, bp, sp) values (39, 'Ice Cream - Turtles Stick Bar', 'vegetables', 40, 50);
    insert into inventory (id, name, type, bp, sp) values (40, 'Pasta - Penne, Rigate, Dry', 'cereals', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (41, 'Bread - French Baquette', 'vegetables', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (42, 'Pop - Club Soda Can', 'fruits', 36, 45);
    insert into inventory (id, name, type, bp, sp) values (43, 'Foam Espresso Cup Plain White', 'fruits', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (44, 'Cheese - Provolone', 'cereals', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (45, 'Lettuce - Romaine', 'fruits', 1, 1.25);
    insert into inventory (id, name, type, bp, sp) values (46, 'Longos - Chicken Curried', 'fruits', 87, 108.75);
    insert into inventory (id, name, type, bp, sp) values (47, 'Wine - Red, Harrow Estates, Cab', 'vegetables', 88, 110);
    insert into inventory (id, name, type, bp, sp) values (48, 'Red Cod Fillets - 225g', 'vegetables', 90, 112.5);
    insert into inventory (id, name, type, bp, sp) values (49, 'Nut - Almond, Blanched, Whole', 'cereals', 7, 8.75);
    insert into inventory (id, name, type, bp, sp) values (50, 'Gelatine Leaves - Envelopes', 'fruits', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (51, 'Fudge - Cream Fudge', 'fruits', 100, 125);
    insert into inventory (id, name, type, bp, sp) values (52, 'Horseradish - Prepared', 'cereals', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (53, 'Wine - Sicilia Igt Nero Avola', 'fruits', 95, 118.75);
    insert into inventory (id, name, type, bp, sp) values (54, 'Burger Veggie', 'fruits', 5, 6.25);
    insert into inventory (id, name, type, bp, sp) values (55, 'Muffin Mix - Morning Glory', 'cereals', 30, 37.5);
    insert into inventory (id, name, type, bp, sp) values (56, 'Steampan - Lid For Half Size', 'fruits', 57, 71.25);
    insert into inventory (id, name, type, bp, sp) values (57, 'Soup - Knorr, Chicken Noodle', 'fruits', 32, 40);
    insert into inventory (id, name, type, bp, sp) values (58, 'Oyster - In Shell', 'vegetables', 86, 107.5);
    insert into inventory (id, name, type, bp, sp) values (59, 'Soup - French Onion', 'cereals', 19, 23.75);
    insert into inventory (id, name, type, bp, sp) values (60, 'Longos - Lasagna Veg', 'cereals', 74, 92.5);
    insert into inventory (id, name, type, bp, sp) values (61, 'Russian Prince', 'cereals', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (62, 'Catfish - Fillets', 'cereals', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (63, 'Pear - Halves', 'vegetables', 50, 62.5);
    insert into inventory (id, name, type, bp, sp) values (64, 'Pears - Fiorelle', 'cereals', 90, 112.5);
    insert into inventory (id, name, type, bp, sp) values (65, 'Shiratamako - Rice Flour', 'cereals', 76, 95);
    insert into inventory (id, name, type, bp, sp) values (66, 'Spring Roll Wrappers', 'cereals', 3, 3.75);
    insert into inventory (id, name, type, bp, sp) values (67, 'Beef - Roasted, Cooked', 'fruits', 64, 80);
    insert into inventory (id, name, type, bp, sp) values (68, 'Gatorade - Xfactor Berry', 'cereals', 12, 15);
    insert into inventory (id, name, type, bp, sp) values (69, 'Lemon Grass', 'fruits', 24, 30);
    insert into inventory (id, name, type, bp, sp) values (70, 'Iced Tea - Lemon, 460 Ml', 'fruits', 11, 13.75);
    insert into inventory (id, name, type, bp, sp) values (71, 'Pastry - Banana Tea Loaf', 'cereals', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (72, 'Yogurt - Plain', 'cereals', 80, 100);
    insert into inventory (id, name, type, bp, sp) values (73, 'Bread Foccacia Whole', 'fruits', 22, 27.5);
    insert into inventory (id, name, type, bp, sp) values (74, 'Pasta - Bauletti, Chicken White', 'cereals', 99, 123.75);
    insert into inventory (id, name, type, bp, sp) values (75, 'Tart Shells - Sweet, 4', 'vegetables', 94, 117.5);
    insert into inventory (id, name, type, bp, sp) values (76, 'Pork Ham Prager', 'vegetables', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (77, 'Vermouth - White, Cinzano', 'fruits', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (78, 'Croissants Thaw And Serve', 'vegetables', 6, 7.5);
    insert into inventory (id, name, type, bp, sp) values (79, 'Wine - Barolo Fontanafredda', 'vegetables', 9, 11.25);
    insert into inventory (id, name, type, bp, sp) values (80, 'Shrimp - 16 - 20 Cooked, Peeled', 'cereals', 45, 56.25);
    insert into inventory (id, name, type, bp, sp) values (81, 'Snails - Large Canned', 'vegetables', 79, 98.75);
    insert into inventory (id, name, type, bp, sp) values (82, 'Cheese - St. Andre', 'fruits', 92, 115);
    insert into inventory (id, name, type, bp, sp) values (83, 'Truffle Shells - White Chocolate', 'vegetables', 79, 98.75);
    insert into inventory (id, name, type, bp, sp) values (84, 'Cheese - Le Cheve Noir', 'vegetables', 42, 52.5);
    insert into inventory (id, name, type, bp, sp) values (85, 'Truffle Shells - White Chocolate', 'cereals', 62, 77.5);
    insert into inventory (id, name, type, bp, sp) values (86, 'Tray - 16in Rnd Blk', 'cereals', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (87, 'Oil - Food, Lacquer Spray', 'vegetables', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (88, 'Plasticknivesblack', 'cereals', 91, 113.75);
    insert into inventory (id, name, type, bp, sp) values (89, 'Toamtoes 6x7 Select', 'fruits', 46, 57.5);
    insert into inventory (id, name, type, bp, sp) values (90, 'Brandy Apricot', 'vegetables', 17, 21.25);
    insert into inventory (id, name, type, bp, sp) values (91, 'Pork - Sausage, Medium', 'fruits', 17, 21.25);
    insert into inventory (id, name, type, bp, sp) values (92, 'V8 Pet', 'fruits', 93, 116.25);
    insert into inventory (id, name, type, bp, sp) values (93, 'Bread Base - Toscano', 'vegetables', 49, 61.25);
    insert into inventory (id, name, type, bp, sp) values (94, 'Beans - Fava, Canned', 'vegetables', 63, 78.75);
    insert into inventory (id, name, type, bp, sp) values (95, 'Pastry - Choclate Baked', 'vegetables', 53, 66.25);
    insert into inventory (id, name, type, bp, sp) values (96, 'Asparagus - Frozen', 'fruits', 98, 122.5);
    insert into inventory (id, name, type, bp, sp) values (97, 'Bread - Ciabatta Buns', 'vegetables', 21, 26.25);
    insert into inventory (id, name, type, bp, sp) values (98, 'Appetizer - Sausage Rolls', 'cereals', 58, 72.5);
    insert into inventory (id, name, type, bp, sp) values (99, 'Truffle Shells - Semi - Sweet', 'fruits', 54, 67.5);
    insert into inventory (id, name, type, bp, sp) values (100, 'Stock - Fish', 'vegetables', 17, 21.25);""")

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
    