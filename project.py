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


#if running from python interpreter, run following code
if __name__ == '__main__':
    app.debug = True #Helpful as server is restarted automatically each time code changes
    app.run(host = '0.0.0.0', port = 5000)
