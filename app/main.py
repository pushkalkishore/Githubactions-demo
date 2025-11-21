from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/sum")
def sum_numbers(a: float, b: float):
    try:
        return {"result": a + b}
    except:
        raise HTTPException(status_code=400, detail="Invalid numbers")


# Api EndPoints
# http://127.0.0.1:8000/health
# http://127.0.0.1:8000/sum?a=3&b=5