from fastapi import FastAPI, WebSocket, WebSocketDisconnect,Request
import cv2
import numpy as np
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

# templates = Jinja2Templates(directory="templates")

# @app.get("/")
# def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/websocket1")
async def websocket_endpoint(websocket: WebSocket):
    # listen for connections
    await websocket.accept()
    #count = 1
    try:
        while True:
            contents = await websocket.receive_bytes()
            arr = np.frombuffer(contents, np.uint8)
            frame = cv2.imdecode(arr, cv2.IMREAD_UNCHANGED)

            ##### modification
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ###############################################
            
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
            #cv2.imwrite("frame%d.png" % count, frame)
            #count += 1
    except WebSocketDisconnect:
        cv2.destroyWindow("frame")
        print("Client disconnected") 


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)