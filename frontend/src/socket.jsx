import { io } from "socket.io-client";

// ✅ Use SAME as fetch (127.0.0.1)
const socket = io("http://127.0.0.1:8000");

export default socket;