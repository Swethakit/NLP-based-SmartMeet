export default function MicButton({ sendMessage }) {

    const startListening = () => {
        const recognition = new window.webkitSpeechRecognition();

        recognition.continuous = true;

        recognition.onresult = (event) => {
            const text =
                event.results[event.results.length - 1][0].transcript;

            sendMessage(text);
        };

        recognition.start();
    };

    return (
        <button onClick={startListening}>
            🎤 Start Speaking
        </button>
    );
}