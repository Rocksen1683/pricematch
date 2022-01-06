import React from "react";
import Footer from "./Footer";

function Team() {
  return (
    <div className="container-fluid team-section" id="teams">
      <div className="section">
        <div className="section-title">
          <h2 className="display-4">The Team</h2>
        </div>
        <div className="card-deck">
          <div className="card">
            <img
              className="card-img-top"
              src="./Prabhav Prefect.jpg"
              alt="Prabhav"
            ></img>
            <div className="card-body">
              <h5 className="card-title">Prabhav Khera</h5>
              <p className="card-text">
                Student at the University of Waterloo, CS 2026.
              </p>
            </div>
          </div>
          <div className="card">
            <img
              className="card-img-top"
              src="./Ekanshh.jpg"
              alt="Prabhav"
            ></img>
            <div className="card-body">
              <h5 className="card-title">Ekanshh Praveen</h5>
              <p className="card-text">
                Student at the University of Waterloo, SE 2026.
              </p>
            </div>
          </div>
          <div className="card">
            <img className="card-img-top" src="./DeepamPic.jpg" alt="Prabhav"></img>
            <div className="card-body">
              <h5 className="card-title">Deepam Dibyajot</h5>
              <p className="card-text">
                Student at the University of Waterloo, CS 2026.
              </p>
            </div>
          </div>
          <div className="card">
            <img
              className="card-img-top"
              src="./Rohit.jpeg"
              alt="Prabhav"
            ></img>
            <div className="card-body">
              <h5 className="card-title">Rohit Bharadwaj</h5>
              <p className="card-text">
                Student at the University of Waterloo, SE 2026.
              </p>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Team;
