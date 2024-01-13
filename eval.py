from vanna.local import LocalContext_OpenAI

def generate_sql(vn: LocalContext_OpenAI, query: str):
    print(vn.generate_sql(query))