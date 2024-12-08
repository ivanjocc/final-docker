export default function MatchResults({ matches }) {
  return (
    <div>
      <h2>Resultados del Matching</h2>
      <ul>
        {matches.map((match, index) => (
          <li key={index}>
            {match.title} - {match.company}
          </li>
        ))}
      </ul>
    </div>
  );
}
