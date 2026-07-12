import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import SchemeForm from "./pages/SchemeForm";
import Results from "./pages/Results";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/form" element={<SchemeForm />} />
        <Route path="/results" element={<Results />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;