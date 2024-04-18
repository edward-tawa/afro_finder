from sqlalchemy.orm import sessionmaker
from models import engine,Scholarship

Session = sessionmaker(bind=engine)

session = Session()

scholarship = session.query(Scholarship).all()
print(scholarship)
# for sc in scholarship:     
#     print('Name:', sc.name)
#     print('Location:' ,sc.location)
#     print('Grant:' ,sc.grantt)
#     print('Deadline Date:' ,sc.deadline)

#     print('#################################################################################')
#     print('#################################################################################')

