import React from "react";
import Banner from './Homepage/Banner';
import Navbar from './Homepage/Navbar';
import Features from './Homepage/Features';
import Team from './Homepage/Team';
import Scroll from './Homepage/Scroll';

function Home() {
  return (
    <div>
      <Navbar />
      <Banner />
      <Features />
      <Team />
      <Scroll showBelow={250} />
    </div>
  );
}

export default Home;
