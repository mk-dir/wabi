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
	bp INT,
	sp INT,
	quantity INT,
        created_at DATE
    );
    insert into inventory (id, name, bp, sp, quantity, created_at) values (1, 'Corn - Cream, Canned', 50, 62.5, 13, '2019-06-02 07:27:25');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (2, 'Cheese - Perron Cheddar', 91, 113.75, 1, '2020-02-07 04:50:30');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (3, 'Muffin Mix - Lemon Cranberry', 12, 15, 5, '2019-02-28 14:32:21');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (4, 'Milk - Buttermilk', 80, 100, 38, '2019-05-18 04:42:49');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (5, 'Island Oasis - Magarita Mix', 19, 23.75, 34, '2019-05-20 16:05:24');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (6, 'Artichokes - Jerusalem', 7, 8.75, 34, '2020-01-07 00:55:49');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (7, 'Liqueur Banana, Ramazzotti', 50, 62.5, 31, '2019-03-18 17:21:46');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (8, 'Soup - Campbells Chili Veg', 88, 110, 52, '2019-11-20 12:33:43');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (9, 'Flavouring - Orange', 7, 8.75, 70, '2019-06-22 01:45:48');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (10, 'Dried Cranberries', 64, 80, 36, '2019-11-27 09:08:42');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (11, 'Fudge - Chocolate Fudge', 30, 37.5, 83, '2019-02-16 17:27:33');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (12, 'Tart - Pecan Butter Squares', 72, 90, 5, '2019-09-25 23:11:03');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (13, 'Ice Cream - Chocolate', 70, 87.5, 46, '2019-08-19 08:30:25');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (14, 'Chocolate - Pistoles, Lactee, Milk', 42, 52.5, 35, '2019-03-23 03:04:44');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (15, 'Vinegar - Red Wine', 43, 53.75, 15, '2019-05-17 22:59:54');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (16, 'Bananas', 65, 81.25, 27, '2019-12-16 09:29:49');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (17, 'Doilies - 10, Paper', 79, 98.75, 74, '2019-09-07 21:57:50');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (18, 'Coffee - Irish Cream', 87, 108.75, 44, '2019-11-13 11:37:20');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (19, 'Wine - Valpolicella Masi', 33, 41.25, 16, '2019-08-18 02:26:47');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (20, 'Cleaner - Lime Away', 24, 30, 44, '2019-02-18 19:01:38');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (21, 'Steampan - Foil', 86, 107.5, 6, '2020-01-21 15:38:16');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (22, 'Sobe - Cranberry Grapefruit', 26, 32.5, 50, '2019-10-12 19:55:02');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (23, 'Venison - Racks Frenched', 8, 10, 2, '2019-07-22 02:27:23');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (24, 'Basil - Primerba, Paste', 81, 101.25, 9, '2019-11-13 21:01:29');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (25, 'White Fish - Filets', 20, 25, 39, '2019-02-27 12:23:53');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (26, 'Wine - Red, Lurton Merlot De', 23, 28.75, 74, '2019-02-16 08:53:52');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (27, 'Wonton Wrappers', 32, 40, 47, '2020-01-24 00:01:32');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (28, 'Pears - Bartlett', 66, 82.5, 87, '2019-12-08 05:49:02');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (29, 'Wasabi Paste', 5, 6.25, 70, '2019-11-09 03:51:36');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (30, 'Quail Eggs - Canned', 74, 92.5, 95, '2019-08-28 16:19:56');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (31, 'Wine - Zinfandel Rosenblum', 80, 100, 39, '2019-02-13 20:02:36');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (32, 'Oxtail - Cut', 97, 121.25, 15, '2019-04-30 22:00:10');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (33, 'Pork Ham Prager', 42, 52.5, 7, '2019-11-11 08:22:50');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (34, 'Wine - Vovray Sec Domaine Huet', 53, 66.25, 68, '2019-10-30 09:32:18');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (35, 'Buffalo - Tenderloin', 5, 6.25, 41, '2019-12-08 12:21:37');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (36, 'Puree - Pear', 61, 76.25, 96, '2019-07-16 04:24:32');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (37, 'Cheese - Fontina', 87, 108.75, 91, '2019-10-31 22:40:38');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (38, 'Cheese - Le Cru Du Clocher', 76, 95, 51, '2019-06-12 00:00:35');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (39, 'Coffee - Colombian, Portioned', 78, 97.5, 78, '2020-01-30 07:50:55');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (40, 'Juice - Lemon', 58, 72.5, 27, '2019-10-27 18:09:33');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (41, 'Sorrel - Fresh', 53, 66.25, 67, '2020-01-08 13:18:00');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (42, 'Wine - Pinot Noir Pond Haddock', 68, 85, 87, '2019-11-08 01:32:25');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (43, 'Sauce - Ranch Dressing', 10, 12.5, 87, '2019-12-13 14:16:39');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (44, 'Mint - Fresh', 87, 108.75, 26, '2019-06-01 17:27:36');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (45, 'Water Chestnut - Canned', 95, 118.75, 68, '2020-01-25 20:35:20');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (46, 'Beer - Original Organic Lager', 20, 25, 98, '2019-03-07 07:47:14');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (47, 'Coffee Guatemala Dark', 9, 11.25, 54, '2019-03-19 05:29:05');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (48, 'Container Clear 8 Oz', 29, 36.25, 53, '2019-05-18 15:16:05');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (49, 'Swiss Chard - Red', 27, 33.75, 48, '2019-08-16 04:34:30');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (50, 'Veal - Round, Eye Of', 16, 20, 1, '2019-02-17 06:56:08');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (51, 'Cod - Black Whole Fillet', 91, 113.75, 36, '2019-04-02 11:08:55');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (52, 'Flour - All Purpose', 49, 61.25, 93, '2019-12-22 03:38:55');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (53, 'Pineapple - Regular', 94, 117.5, 38, '2019-11-22 23:40:06');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (54, 'Pepper - Black, Ground', 22, 27.5, 49, '2019-06-21 09:45:29');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (55, 'Sauce - Bernaise, Mix', 32, 40, 90, '2019-02-14 18:04:45');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (56, 'Stock - Fish', 40, 50, 17, '2019-12-24 04:40:18');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (57, 'Couscous', 11, 13.75, 28, '2019-08-10 16:42:50');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (58, 'Trueblue - Blueberry Cranberry', 22, 27.5, 60, '2019-06-24 11:02:45');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (59, 'Soda Water - Club Soda, 355 Ml', 59, 73.75, 16, '2019-11-29 21:30:28');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (60, 'Beef - Top Sirloin', 51, 63.75, 24, '2019-11-28 06:22:41');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (61, 'Tea - Decaf Lipton', 29, 36.25, 43, '2019-04-22 13:41:08');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (62, 'Creamers - 10%', 66, 82.5, 29, '2019-06-06 08:17:04');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (63, 'Wine - Riesling Alsace Ac 2001', 39, 48.75, 20, '2019-11-10 06:19:25');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (64, 'Wine - Mondavi Coastal Private', 14, 17.5, 68, '2019-10-31 17:45:11');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (65, 'Lettuce - Romaine, Heart', 10, 12.5, 55, '2019-04-10 00:39:25');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (66, 'Carbonated Water - Blackberry', 91, 113.75, 77, '2019-06-03 09:32:26');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (67, 'Chicken - Whole Fryers', 94, 117.5, 35, '2019-10-28 01:42:49');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (68, 'Veal - Bones', 72, 90, 40, '2019-04-21 02:09:30');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (69, 'Steamers White', 100, 125, 62, '2019-12-10 00:03:06');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (70, 'Tea - Mint', 83, 103.75, 72, '2019-11-14 11:58:34');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (71, 'Flour - Cake', 30, 37.5, 28, '2019-09-01 03:07:13');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (72, 'Tart Shells - Barquettes, Savory', 13, 16.25, 57, '2019-07-25 13:20:13');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (73, 'Carrots - Mini, Stem On', 79, 98.75, 15, '2019-09-04 03:17:47');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (74, 'Onions - Spanish', 88, 110, 28, '2019-07-27 03:58:04');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (75, 'Cheese - Brick With Onion', 88, 110, 94, '2019-05-19 04:41:47');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (76, 'Dill Weed - Dry', 26, 32.5, 92, '2019-03-12 15:23:57');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (77, 'Coconut - Shredded, Sweet', 47, 58.75, 39, '2019-10-21 09:09:33');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (78, 'Pepperoni Slices', 100, 125, 71, '2019-03-03 19:53:27');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (79, 'Lamb - Racks, Frenched', 72, 90, 77, '2020-01-20 21:09:20');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (80, 'Langers - Cranberry Cocktail', 39, 48.75, 80, '2020-01-31 03:27:37');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (81, 'Samosa - Veg', 37, 46.25, 58, '2019-08-28 00:30:09');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (82, 'Anchovy Paste - 56 G Tube', 63, 78.75, 83, '2020-01-08 10:52:35');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (83, 'Chocolate - Milk, Callets', 17, 21.25, 91, '2019-12-29 05:16:39');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (84, 'Tea - Herbal Sweet Dreams', 61, 76.25, 78, '2019-07-09 19:09:47');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (85, 'Tofu - Firm', 22, 27.5, 82, '2019-07-21 21:59:50');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (86, 'Beef - Kindney, Whole', 51, 63.75, 91, '2019-10-14 14:29:53');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (87, 'Rum - Light, Captain Morgan', 49, 61.25, 8, '2019-09-09 02:59:51');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (88, 'Steampan Lid', 28, 35, 4, '2019-06-30 20:54:04');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (89, 'Squid - Tubes / Tenticles 10/20', 48, 60, 57, '2019-12-14 07:50:40');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (90, 'Wine - Chianti Classica Docg', 31, 38.75, 91, '2019-06-29 23:37:19');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (91, 'Bread Sour Rolls', 41, 51.25, 58, '2020-01-20 05:45:10');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (92, 'Coffee - Beans, Whole', 54, 67.5, 57, '2019-11-23 23:32:18');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (93, 'Wasabi Powder', 51, 63.75, 33, '2019-11-21 21:46:30');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (94, 'Five Alive Citrus', 3, 3.75, 90, '2019-07-21 03:43:46');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (95, 'Lettuce - Radicchio', 25, 31.25, 93, '2019-08-19 09:31:52');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (96, 'Pasta - Rotini, Dry', 17, 21.25, 74, '2019-06-24 14:55:52');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (97, 'Bagelers - Cinn / Brown', 41, 51.25, 74, '2019-11-29 20:45:10');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (98, 'Ice Cream Bar - Hageen Daz To', 89, 111.25, 14, '2019-07-05 09:42:39');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (99, 'Snapple - Mango Maddness', 66, 82.5, 72, '2019-10-27 06:09:41');
    insert into inventory (id, name, bp, sp, quantity, created_at) values (100, 'Cheese - Brie Roitelet', 29, 36.25, 20, '2019-05-24 16:09:27');""")

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
    