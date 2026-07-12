import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./SchemeForm.css";

function SchemeForm() {
  const [age, setAge] = useState("");
  const [income, setIncome] = useState("");
  const [occupation, setOccupation] = useState("");
  const [gender, setGender] = useState("");
  const [casteCategory, setCasteCategory] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    setErrorMessage("");

    try {
      const response = await fetch("https://setu-welfare-scheme-recommender.onrender.com/match",  {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          age: Number(age),
          income: Number(income),
          occupation: occupation,
          gender: gender,
          caste_category: casteCategory,
        }),
      });

      if (!response.ok) {
        throw new Error("Server responded with an error");
      }

      const data = await response.json();
      navigate("/results", { state: { matches: data } });
    } catch (error) {
      console.error("Error fetching matches:", error);
      setErrorMessage(
        "We couldn't connect to the server. Please check your connection and try again."
      );
    }
  }

  return (
    <div className="form-page">
      <div className="form-card">
        <h1>Check Your Eligibility</h1>
        <p className="form-subtitle">Fill in your details to see matched welfare schemes</p>
        {errorMessage && <p className="form-error">{errorMessage}</p>}

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Age</label>
            <input
              type="number"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Annual Income (₹)</label>
            <input
              type="number"
              value={income}
              onChange={(e) => setIncome(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label>Occupation</label>
            <select
              value={occupation}
              onChange={(e) => setOccupation(e.target.value)}
              required
            >
              <option value="">-- Select --</option>
              <option value="Farmer">Farmer</option>
              <option value="Student">Student</option>
              <option value="Self-employed/Entrepreneur">Self-employed/Entrepreneur</option>
              <option value="Unemployed">Unemployed</option>
              <option value="Artisan/Craftsperson">Artisan/Craftsperson</option>
              <option value="Fisherperson">Fisherperson</option>
              <option value="Other">Other</option>
            </select>
          </div>

          <div className="form-group">
            <label>Gender</label>
            <select
              value={gender}
              onChange={(e) => setGender(e.target.value)}
              required
            >
              <option value="">-- Select --</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
              <option value="Other">Other</option>
            </select>
          </div>

          <div className="form-group">
            <label>Category</label>
            <select
              value={casteCategory}
              onChange={(e) => setCasteCategory(e.target.value)}
              required
            >
              <option value="">-- Select --</option>
              <option value="General">General</option>
              <option value="SC">SC</option>
              <option value="ST">ST</option>
              <option value="OBC">OBC</option>
              <option value="Minority">Minority</option>
            </select>
          </div>

          <button type="submit" className="btn-primary">Find My Schemes</button>
        </form>
      </div>
    </div>
  );
}

export default SchemeForm;