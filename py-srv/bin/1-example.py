import json
from surrealdb import Surreal

async def query(sql):
    """Example of how to use the SurrealDB client."""
    async with Surreal("ws://db:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "pass"})
        await db.use("test", "test")
        x = await db.query(sql)
        return x[0]['result']
        # In SurrealQL you can do a direct insert 
        # and the table will be created if it doesn't exist
    
async def insert():
    results = []
    records = [
        {'breed': 'test_breed1', 'color': 'test_color1', 'my_id': '1'},
        {'breed': 'test_breed2', 'color': 'test_color2', 'my_id': '2'},
        {'breed': 'test_breed3', 'color': 'test_color3', 'my_id': '3'},
        {'breed': 'test_breed4', 'color': 'test_color4', 'my_id': '4'},
    ]
    for record in records:
        sql = "insert into person {"
        for k, v in record.items():
            sql += f"{k}: '{v}',"
        sql += "};"
        results.append(await query(sql))
    return results

async def select():
    return await query("select * from person")

async def select_by_filter(val):
    return await query(f"select * from person where my_id = '{val}'")

async def update(val):
    sql = f"update person set breed='test_breed5', color='test_color5', id='5' where id = '{val}';"
    return await query(sql)

async def delete(val):
    return await query(f"delete person where my_id = '{val}'")

async def main():
    print(await insert())
    print(await select())
    print(await select_by_filter('1'))
    print(await update('1'))
    print(await delete('2'))
    print(await select())

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())