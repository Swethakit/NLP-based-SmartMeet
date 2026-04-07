export default function TranscriptPanel({ transcript }) {
    return (
        <div>
            <h3>Transcript</h3>
            {transcript.map((line, index) => (
                <p key={index}>{line}</p>
            ))}
        </div>
    );
}