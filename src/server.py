from fastapi import FastAPI
from client import get_client

app = FastAPI()

client = get_client()

@app.get("/metadata/{video_id}")
async def get_metadata(video_id: str):
    try:
        metadata = client.video.get_video(video_id)
        return metadata
    except Exception as e:
        return {"error": str(e)}

@app.get("/comments/{video_id}")
async def get_comments(video_id: str):
    try:
        watch_data = client.video.watch.get_watch_data(video_id)
        comments = client.video.watch.get_comments(watch_data)
        return comments
    except Exception as e:
        return {"error": str(e)}