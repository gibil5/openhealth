import abc

from architecture.domain import model 

# ------------------------------------ Class ------------------------------------------
class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError

# ------------------------------------ Class ------------------------------------------
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        print('SqlAlchemyRepository - List')
        #return self.session.query(model.Batch).all()
        #print(self.session.query(model.Batch).all())
        print(self.session.query(model.Batch))
        return 'fake'