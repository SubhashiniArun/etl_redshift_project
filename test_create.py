from sqlalchemy import create_engine
from app.models import Base

engine = create_engine("mysql+pymysql://root:checkmysql@localhost:3306/etl_project")
Base.metadata.create_all(engine)