#!/usr/bin/python3
from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('postgresql://catalog:password@localhost/catalog')

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

# Delete all the rows

session.query(User).delete()
session.commit()

session.query(Item).delete()
session.commit()

session.query(Category).delete()
session.commit()
