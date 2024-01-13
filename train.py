from vanna.local import LocalContext_OpenAI
import utils


def train_model(ddl: str, doc: str):
    vn = LocalContext_OpenAI({"api_key": utils.API_KEY})
    vn.train(ddl=ddl)
    vn.train(documentation=doc)
    return vn