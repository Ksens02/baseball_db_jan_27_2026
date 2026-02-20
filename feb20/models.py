from sqlmodel import SQLModel, Field, create_engine

#id can be int and None becaus we are saying "we're not going to set the id, the behind the scenes program will have to do it automatically"
class Faculty(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    firstname: str
    lastname: str
    age: int | None = None

engine = create_engine("sqlite:///department.db")

SQLModel.metadata.create_all(engine)