from fastapi import FastAPI, Request

import time

app = FastAPI()


@app.get("/demo/echo/seconds/{seconds}")
async def echo_seconds(seconds: int):
    time.sleep(seconds)
    return {
      "seconds": seconds,
      "seconds_in_array": [seconds, seconds, seconds],
      "seconds_with_string": str(seconds) + "_demo",
    }


@app.get("/demo/echo/request/{seconds}")
async def echo_request(seconds: int, rq: Request):
    time.sleep(seconds)
    return {
        "seconds": seconds,
        "request": {
            "client": {"host": rq.client.host},
            "headers": rq.headers,
            "query_params": rq.query_params,
            "path_params": rq.path_params,
            "cookies": rq.cookies,
        },
    }


@app.get("/")
async def root():
    return {"message": "Hello World"}



