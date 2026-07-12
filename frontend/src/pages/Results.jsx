import { useLocation, Link } from "react-router-dom";
import "./Results.css";

function Results() {
  const location = useLocation();
  const matches = location.state?.matches || [];

  return (
    <div className="results-page">
      <div className="results-header">
        <h1>Your Matched Schemes</h1>
        {matches.length === 0 ? (
          <p>No matching schemes found, or no data was submitted.</p>
        ) : (
          <p>You are eligible for <strong>{matches.length}</strong> scheme(s):</p>
        )}
      </div>

      <div className="results-list">
        {matches.map((scheme) => (
          <div key={scheme.scheme_id} className="scheme-card">
            <div className="scheme-card-header">
              <h2>{scheme.name}</h2>
              <span className="scheme-badge">{scheme.level}</span>
            </div>
            <p className="scheme-category">{scheme.category}</p>
            <p className="scheme-benefit"><strong>Benefit:</strong> {scheme.benefits}</p>
            <p className="reasons-label">Why you qualify:</p>
            {scheme.reasons.length > 0 ? (
              <ul className="reasons-list">
                {scheme.reasons.map((reason, index) => (
                  <li key={index}>{reason}</li>
                ))}
              </ul>
            ) : (
              <p className="no-restrictions">
                This scheme has no specific restrictions — open to all eligible Karnataka residents.
              </p>
            )}
            {scheme.official_link && (
              <a href={scheme.official_link} target="_blank" rel="noopener noreferrer" className="official-link">
                Visit official page
              </a>
            )}
          </div>
        ))}
      </div>

      <div className="results-footer">
        <Link to="/form" className="btn-secondary">Check Again</Link>
      </div>
    </div>
  );
}

export default Results;