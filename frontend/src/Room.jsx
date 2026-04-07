import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import socket from "./socket.jsx";
import TranscriptPanel from "./components/TranscriptPanel.jsx";
import TopicPanel from "./components/TopicPanel.jsx";
import Avatar from "./components/Avatar.jsx";
import MicButton from "./components/MicButton.jsx";
import "./style.css";

export default function Room() {
    const { roomId } = useParams();

    const [transcript, setTranscript] = useState([]);
    const [topics, setTopics] = useState([]);
    const [sentiment, setSentiment] = useState("NEUTRAL");
    const [pdfLink, setPdfLink] = useState("");

    useEffect(() => {
        socket.emit("join_room", { room: roomId });

        socket.on("analysis", (data) => {
            setTranscript(prev => [...prev, data.text]);
            setTopics(data.topics);
            setSentiment(data.sentiment.label);
        });

        socket.on("meeting_report", (data) => {
            setPdfLink(`http://127.0.0.1:8000/files/${data.file}`);
        });

        return () => {
            socket.off("analysis");
            socket.off("meeting_report");
        };
    }, [roomId]);

    const sendMessage = (text) => {
        socket.emit("send_message", {
            room: roomId,
            text: text
        });
    };

    const endMeeting = () => {
        socket.emit("end_meeting", { room: roomId });
    };

    return (
        <div className="room-container">

            {/* LEFT SIDE */}
            <div className="left-panel">

                <div className="top-bar">
                    <h2>Room: {roomId}</h2>
                    <button className="btn btn-danger" onClick={endMeeting}>
                        End Meeting
                    </button>
                </div>

                <Avatar sentiment={sentiment} />

                <MicButton sendMessage={sendMessage} />

                <div className="transcript-box">
                    <TranscriptPanel transcript={transcript} />
                </div>

                {pdfLink && (
                    <a className="download" href={pdfLink} download>
                        Download Report 📄
                    </a>
                )}

            </div>

            {/* RIGHT SIDE */}
            <div className="right-panel">
                <h3>Topics</h3>
                <TopicPanel topics={topics} />
            </div>

        </div>
    );
}