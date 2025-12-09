from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://al_ml_learning_user:al_ml_learning_password@localhost:5433/al_ml_learning_db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


if __name__=="__main__":
    # Create all tables
    # Base.metadata.create_all(engine)
    # print("Tables created successfully!")
    # student1 = Student(name="John", age=10, grade="Year 5")
    # student2 = Student(name= "Hanze", age =5, grade="Year 1")
    student3 = Student(name= "Hanze", age =5, grade="Year 1")
    student4 = Student(name= "Moti", age =50, grade="Year 7")
    student5 = Student(name= "Ramu", age =15, grade="Year 10")
    student6 = Student(name= "Supandi", age =25, grade="Year 11")


    # session.add(student1)
    # session.add(student2)
    # session.add(student3)
    # session.add(student4)
    # session.add(student5)
    # session.add(student6)
    #
    # session.commit()

    # students = session.query(Student)

    # students = session.query(Student).order_by(Student.name)

    # students = session.query(Student).filter(Student.name=="John")

    students = session.query(Student).filter(or_(Student.name == "John",Student.name == "Moti"))
    for s in students:
        print(s.name)

    student = session.query(Student).filter(or_(Student.name == "John", Student.name == "Moti")).count()
    print(student)

    john_student = session.query(Student).filter(Student.name=="Moti").first()
    if john_student:
        print("student found",john_student.name)
        session.delete(john_student)
        session.commit()

        updated_name = session.query(Student).filter(Student.name=="Moti").first()
        print(updated_name.name if updated_name else "not found again")
    else:
        print("No student named John found in database")

    session.close()
