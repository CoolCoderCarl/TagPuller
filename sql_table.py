from datetime import datetime
from importlib import resources

from sqlalchemy import Column, Integer, String, ForeignKey, Table, Text, DateTime, Identity, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Tags(Base):
    __tablename__ = "test_table"
    uid = Column(Integer, primary_key=True)
    domain = Column(Text)
    url_from_ui = Column(String)
    timestamp = Column(DateTime)
    tags_data = Column(String)


def session():
    """Main entry point of program"""
    # Connect to the database using SQLAlchemy
    # with resources.path(
    #     "test.db"
    # ) as sqlite_filepath:
    engine = create_engine(f"sqlite:///test.db")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    return session


def add_new_tags(session, domain, url_from_ui, tags_data):
    """Adds a new book to the system"""

    t1 = Tags(domain=domain, url_from_ui=url_from_ui, timestamp=datetime.now(), tags_data=tags_data)

    session.add(t1)
    session.commit()


if __name__ == '__main__':
    session()
    add_new_tags(session(), domain="google", url_from_ui="www.google.com", tags_data="data_of_tags")
    pass

