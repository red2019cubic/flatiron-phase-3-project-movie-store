from .base import Base
from sqlalchemy import Table, Integer, ForeignKey, Column


movie_actor = Table(
    "movies_actors", Base.metadata,
    Column("id", Integer, primary_key=True),
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id')),
)