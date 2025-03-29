from fastapi import FastAPI
from routers import routerPred


app = FastAPI()
app.include_router(routerPred.router)


if __name__=="__main__":
    app.run()