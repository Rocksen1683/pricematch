import React from "react";
import "./styles.css";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div className="navbar navbar-expand-md navbar-sticky-top bg-faded navbar-center">
      <div className="container">
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarTogglerDemo01"
          aria-controls="navbarTogglerDemo01"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="navbar-collapse navbar-collapse" id="navbarResponsive">
          <Link to="/" className="navbar-brand" href="#">
            PriceMatch
          </Link>
          <ul className="navbar-nav m-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link to="/" className="nav-link" href="#">
                Home
              </Link>
            </li>
            <li className="nav-item">
              <a href="#teams" className="nav-link">
                About Us
              </a>
            </li>
            <li className="nav-item">
              <Link to="/contact" className="nav-link" href="#">
                Contact Us
              </Link>
            </li>
          </ul>
          <Link to="/pricematch" className="btn btn-outline-info">Try It Out!</Link>
          {/* <button className="btn btn-light">Take a photo!</button> */}
        </div>
      </div>
    </div>
  );
}

export default Navbar;
