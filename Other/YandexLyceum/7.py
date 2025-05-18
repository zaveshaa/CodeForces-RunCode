from sqlalchemy import func

db_name = input().strip()

global_init(db_name)
session = create_session()

results = (
    session.query(User)
    .join(Jobs)
    .join(Department)
    .filter(Department.id == 1)
    .group_by(User.id)
    .having(func.sum(Jobs.work_size) > 25)
)

for user in results:
    print(f"{user.surname} {user.name}")