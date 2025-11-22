from fastapi import FastAPI, HTTPException

app = FastAPI()

## Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}


## Addition of two numbers
@app.get("/sum")
def sum_numbers(a: float, b: float):
    try:
        return {"result": a + b}
    except:
        raise HTTPException(status_code=400, detail="Invalid numbers")

## Multiplication of two numbers
@app.get("/product")
def multiply_numbers(a: float, b: float):
    try:
        return {"result": a * b}
    except:
        raise HTTPException(status_code=400, detail="Invalid numbers")


# ## Division of two numbers
# @app.get("/divide")
# def divide_numbers(a: float, b: float):
#     try:
#         if b == 0:
#             raise HTTPException(status_code=400, detail="Division by zero is not allowed")
#         return {"result": a / b}
#     except:
#         raise HTTPException(status_code=400, detail="Invalid numbers")

# Api EndPoints
# http://127.0.0.1:8000/health
# http://127.0.0.1:8000/sum?a=3&b=5
# http://127.0.0.1:8000/product?a=7&b=8