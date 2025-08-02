import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import OperatorSelection from './pages/operators_selection';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <Router>
      <nav>
        <Link to="/ops">Operators</Link>
      </nav>
      <Routes>
        <Route path="/ops" element={<OperatorSelection />} />
      </Routes>
    </Router>
  );
}

export default App;
