export default function LeadCard({ name, email }) {
    return (
        <div className="card">
            <h3>{name}</h3>
            <p>{email}</p>
        </div>
    );
}