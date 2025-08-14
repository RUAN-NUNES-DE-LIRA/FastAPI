from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/message')
async def message():
    return {'msg': 'python'}

if __name__ == '__main__':

    uvicorn.run('main:app',
                host='localhost',
                port=8000,
                log_level='info',
                reload=True)