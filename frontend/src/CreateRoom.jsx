import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./style.css";

export default function CreateRoom() {
    const [room, setRoom] = useState("");
    const navigate = useNavigate();

    const createRoom = async () => {
        try {
            const res = await fetch("http://127.0.0.1:8000/create-room");
            const data = await res.json();
            navigate(`/room/${data.room}`);
        } catch (error) {
            console.error("Error:", error);
        }
    };

    const joinRoom = () => {
        if (room.trim() !== "") {
            navigate(`/room/${room}`);
        }
    };

    return (
        <div className="container">
            <div className="card">
                <h1 className="title">SmartMeet 🚀</h1>
                <p className="subtitle">AI-powered meeting assistant</p>

                <button className="btn btn-primary" onClick={createRoom}>
                    + Create Room
                </button>

                <div className="input-group">
                    <input
                        className="input"
                        placeholder="Enter Room ID"
                        value={room}
                        onChange={(e) => setRoom(e.target.value)}
                    />
                    <button className="btn btn-success" onClick={joinRoom}>
                        Join
                    </button>
                </div>
            </div>
        </div>
    );
}