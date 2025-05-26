#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

# Setup database connection
engine = create_engine('sqlite:///freebie_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create companies
c1 = Company(name="TechCorp", founding_year=2005)
c2 = Company(name="DevWorks", founding_year=2012)

# Create developers
d1 = Dev(name="Alice")
d2 = Dev(name="Bob")
d3 = Dev(name="Charlie")

# Add to session and commit
session.add_all([c1, c2, d1, d2, d3])
session.commit()

# Create freebies using give_freebie 
f1 = c1.give_freebie(session, d1, "Sticker", 5)
f2 = c2.give_freebie(session, d1, "T-Shirt", 15)
f3 = c1.give_freebie(session, d2, "Notebook", 10)
f4 = c2.give_freebie(session, d3, "Mug", 12)

# Confirm data
print(f"{d1.name} owns a {f1.item_name} from {f1.company.name}.")
print(f"{d1.name} owns a {f2.item_name} from {f2.company.name}.")
print(f"{d2.name} owns a {f3.item_name} from {f3.company.name}.")
print(f"{d3.name} owns a {f4.item_name} from {f4.company.name}.")



