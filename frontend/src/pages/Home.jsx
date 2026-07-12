import { Link } from "react-router-dom";
import "./Home.css";

function Home() {
  return (
    <div className="home-container">
      <div className="hero">
        <h1>SETU</h1>
        <p className="tagline">
          AI-Driven Welfare Scheme Discovery and Eligibility Recommendation System
        </p>
        <p className="description">
          Discover government welfare schemes you're eligible for — instantly,
          with clear explanations, tailored for Karnataka citizens.
        </p>
        <Link to="/form">
          <button className="btn-primary">Check Your Eligibility</button>
        </Link>
      </div>
    </div>
  );
}

export default Home;