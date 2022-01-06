import React from "react";

function Features() {
  return (
    <div className="contaniner-fluid" id="features-page">
      <div className="features container">
        <div className="feature">
          <div className="feature-img">
            <img src="./Money.png" alt="Save Money" />
          </div>
          <div className="feature-description">
            Save money on groceries and day-to-day purchases.
          </div>
        </div>
        <div className="feature">
          <div className="feature-img">
            <img src="./Explore.png" alt="Save Money" />
          </div>
          <div className="feature-description">
            Get the best deals on your daily products.
          </div>
        </div>
        <div className="feature">
          <div className="feature-img">
            <img src="./Shop.png" alt="Save Money" />
          </div>
          <div className="feature-description">Become a smarter consumer</div>
        </div>
      </div>
    </div>
  );
}

export default Features;
