import React from "react";
import { NavLink } from "react-router-dom";

function Navigation() {
  return (
    <div className="navigation">
      <nav className="navbar navbar-expand navbar-light bg-light">
        <div className="container">
          <NavLink className="navbar-brand" to="/">
            Straßenverkehrsamt
          </NavLink>
          <div>
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <NavLink className="nav-link" to="/">
                  Übersicht
                  <span className="sr-only">(current)</span>
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/Fahrzeuge">
                  Fahrzeuge
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/Fuehrerschein">
                  Führerschein
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/StVO">
                  StVO
                </NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default Navigation;