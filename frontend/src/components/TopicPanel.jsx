export default function TopicPanel({ topics }) {
    return (
        <div>
            <h3>Topics</h3>
            {topics.map((topic, index) => (
                <p key={index}>{topic}</p>
            ))}
        </div>
    );
}