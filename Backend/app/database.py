from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuration Snowflake
SNOWFLAKE_URL = (
    "snowflake://{user}:{password}@{account}/{database}/{schema}"
    .format(
        user="YOUR_USER",
        password="YOUR_PASSWORD",
        account="YOUR_ACCOUNT.snowflakecomputing.com",
        database="recruitment_db",
        schema="public"
    )
)

engine = create_engine(SNOWFLAKE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dépendance FastAPI pour obtenir une session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
