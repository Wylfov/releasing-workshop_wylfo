from sqlmodel import Session, create_engine, text

engine = create_engine("postgresql://neondb_owner:npg_8NkP0FOwTYIc@ep-icy-base-ba5iipz9-pooler.c-8.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
session = Session(engine)

session.exec(text("INSERT INTO todo (title, done) VALUES ('Buy milk', False)"))
session.commit()

session.exec(text("SELECT * FROM todo")).all()
