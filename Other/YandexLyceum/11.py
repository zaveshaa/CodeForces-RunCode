# 2 variola вариола
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, joinedload

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    surname = Column(String(255))
    name = Column(String(255))
    department = Column(Integer, ForeignKey('departments.id'))
    jobs = relationship("Jobs", foreign_keys="Jobs.team_leader")


class Jobs(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    team_leader = Column(Integer, ForeignKey('users.id'))
    work_size = Column(Integer)


class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))


def global_init(db_file):
    engine = create_engine(f'sqlite:///{db_file}?check_same_thread=False')
    Base.metadata.bind = engine
    return sessionmaker(bind=engine)


def main():
    db_name = input().strip()
    Session = global_init(db_name)
    session = Session()

    dept_id = 1

    result = (
        session.query(User)
        .join(Jobs, User.id == Jobs.team_leader)
        .join(Department, Department.id == User.department)
        .filter(Department.id == dept_id)
        .group_by(User.id)
        .having(func.sum(Jobs.work_size) > 25)
        .all()
    )

    for user in result:
        print(f"{user.surname} {user.name}")


if __name__ == '__main__':
    main()
