import socketio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from nlp import analyze_sentiment
from topic import detect_topics
from summary import summarize
from pdf import generate_pdf
from room_manager import create_room

# Socket setup
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*"
)

app = FastAPI()

# CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

socket_app = socketio.ASGIApp(sio, app)

# Serve generated PDF files
app.mount("/files", StaticFiles(directory="files"), name="files")

# In-memory storage
transcripts = {}

# ------------------ ROUTES ------------------

@app.get("/")
def home():
    return {"message": "SmartMeet Backend Running 🚀"}


@app.get("/create-room")
def new_room():
    room = create_room()
    transcripts[room] = []
    return {"room": room}


# ------------------ SOCKET EVENTS ------------------

@sio.event
async def connect(sid, environ):
    print("User connected:", sid)


@sio.event
async def join_room(sid, data):
    room = data["room"]

    if room not in transcripts:
        transcripts[room] = []

    await sio.enter_room(sid, room)
    await sio.emit("user_joined", {"sid": sid}, room=room)


@sio.event
async def send_message(sid, data):
    room = data["room"]
    text = data["text"]

    if room not in transcripts:
        transcripts[room] = []

    transcripts[room].append(text)

    sentiment = analyze_sentiment(text)
    topics = detect_topics(" ".join(transcripts[room]))

    await sio.emit(
        "analysis",
        {
            "text": text,
            "sentiment": sentiment,
            "topics": topics
        },
        room=room
    )


@sio.event
async def end_meeting(sid, data):
    room = data["room"]

    if room not in transcripts:
        return

    full_text = " ".join(transcripts[room])

    short_text = full_text[:1000]

    topics = detect_topics(short_text)
    summary = summarize(short_text)

    pdf_file = generate_pdf(transcripts[room], topics, summary)

    await sio.emit(
        "meeting_report",
        {
            "summary": summary,
            "topics": topics,
            "file": pdf_file
        },
        room=room
    )

    del transcripts[room]