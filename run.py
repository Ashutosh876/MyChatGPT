import uvicorn

if __name__ == "__main__":
    uvicorn.run("chat.main:app", reload=True)
