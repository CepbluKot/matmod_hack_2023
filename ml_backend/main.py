import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


from settingWeb import app
import uvicorn


from routers.predict.predictRouter import router as RouterML


app.include_router(RouterML)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
