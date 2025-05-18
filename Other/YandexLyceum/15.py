from sqlalchemy import func
from sqlalchemy.orm import joinedload


def main():
    db_name = input().strip()
    global_init(db_name)
    session = create_session()

    department_id = 1

    result = (
        session.query(User)
        .join(Jobs)
        .join(Department)
        .filter(Department.id == department_id)
        .group_by(User.id)
        .having(func.sum(Jobs.work_size) > 25)
        .all()
    )

    for user in result:
        print(f"{user.surname} {user.name}")


if __name__ == "__main__":
    main()
