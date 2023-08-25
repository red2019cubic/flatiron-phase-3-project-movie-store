from sqlalchemy.orm import declative_base, create_engine, relationship
from sqlalchemy import Column, Integer, String, date, Table,ForeignKey



Base = declative_base()

movie_actor = Table(
    "movies_actors", Base.metadata,
    Column("id", Integer, primary_key=True),
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id')),
)

class Movie(Base):
    __tablename__ = "movies"

    id = Column("movie_id", Integer(), primary_key=True)
    title = Column("title", String(), nullable=False)
    year = Column("year", Integer(), nullable=False)
    actors = relationship("actors", secondary=movie_actor, backref="The_movies")

    def __repr__(self):
        return "<Movie " \
            + f"id={self.id}, " \
            + f"title={self.title}, " \
            + f"year={self.year}, " \
            + ">"


class Actor(Base):
    __tablename__ = "actors"

    id = Column("actor_id", Integer(), primary_key=True)
    first_name = Column("first_name", String(), nullable=False)
    last_name = Column("last_name", String(), nullable=False)
    dob = Column("date_of_birth", date(), nullable=False)
    movies = relationship("movies", secondary=movie_actor, backref="The_actors")

    def __repr__(self):
        return "<Actor " \
            + f"id={self.id}, " \
            + f"first_name={self.first_name}" \
            + f"last_name={self.last_name}" \
            + f"dob={self.dob}" \
            + ">"



