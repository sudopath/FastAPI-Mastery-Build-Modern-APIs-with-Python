from databases import Database
from fastapi import FastAPI

app = FastAPI()
database =Database("sqlite:///test.db")


async def create_table():
    query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INTEGER PRIMARY KEY,
            name TEXT
            
        );
    """

    await database.execute(query)

    count  = await database.fetch_val("SELECT count(*) FROM example_table")
    
    if count == 0:
        await database.execute("INSERT INTO example_table (name) VALUES ('John Doe')")
        await database.execute("INSERT INTO example_table (name) VALUES ('Alice Doe')")


@app.on_event("startup")
async def startup():
    await database.connect()
    await create_table()


@app.on_event("shutdown")
async def disconnect_from_db():
    await database.disconnect()


@app.get("/async-db")
async def async_db():
    query = "SELECT * FROM example_table"
    rows = await database.fetch_all(query)
    return {"data": rows}