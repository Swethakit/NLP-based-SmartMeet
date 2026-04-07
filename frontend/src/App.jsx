import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CreateRoom from "./CreateRoom.jsx";
import Room from "./Room.jsx";

export default function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<CreateRoom />} />
                <Route path="/room/:roomId" element={<Room />} />
            </Routes>
        </Router>
    );
}