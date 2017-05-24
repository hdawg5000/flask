from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#decorator - when server recevies request that matches arg,
#proceeding method is run (hello world)
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += "</br>"
        output += i.price + "</br>" + i.description + "</br></br>"
    return output

@app.route('/restaurant/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    output = ''
    output += "<html><body><h1>Create a new restaurant</h1>"
    output += "<form method='post' enctype='multipart/form-data'\
     action='/restaurants/new/'>"
    output += "<input type='text' placeholder"
    return "page to create a new menu item. Task 1 complete!"

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


#if running from python interpreter, run following code
if __name__ == '__main__':
    app.debug = True #Helpful as server is restarted automatically each time code changes
    app.run(host = '0.0.0.0', port = 5000)
