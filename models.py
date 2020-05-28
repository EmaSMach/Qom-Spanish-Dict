from sqlalchemy import Column, String, Integer, create_engine
from db import Base

from db import session


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    qom = Column(String(), nullable=True)
    dfs = Column(String(), nullable=True)
    syn = Column(String(), nullable=True)
    var = Column(String(), nullable=True)
    see = Column(String(), nullable=True)

    def __init__(self, id, qom, dfs, syn, var, see):
        self.id = id
        self.qom = qom
        self.dfs = dfs
        self.syn = syn
        self.var = var
        self.see = see

    def to_dict(self):
        wd = {'id' : self.id,
              'qom': self.qom,
              'dfs': self.dfs,
              'syn': self.syn,
              'var': self.var,
              'see': self.see}
        return wd

    def to_list(self):
        return [self.id, self.qom, self.dfs, self.syn, self.var, self.see,]

    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        obj = session.query(Word).filter_by(id=self.id)
        session.delete(obj)
        session.commit()

    def __repr__(self):
        return self.qom


Base.metadata.create_all()
