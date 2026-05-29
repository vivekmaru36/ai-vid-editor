from fastapi import FastAPI


app=FastAPI(
    title="AI Reel Editor",
    version="1.0.0"
    )

@app.get("/")
async def root():
    return {
        "status":"Running",
        "service":"ai-reel-editor"
    }
