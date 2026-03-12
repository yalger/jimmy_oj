from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.models.user import User

def create_default_admin(db: Session):

    # 检查是否已有 admin 用户
    admin_user = db.query(User).filter_by(username="admin").first()
    if admin_user:
        return

    # 创建默认管理员
    admin_user = User(
        username="admin",
        password_hash=get_password_hash("admin"),
        is_active=True,
    )


    db.add(admin_user)
    db.commit()

    print("Default admin created: username=admin password=admin")
    print("⚠ Please change default admin password after first login!")

def init_seed_data(db: Session):

    create_default_admin(db=db)

    print("Seed data initialized.")