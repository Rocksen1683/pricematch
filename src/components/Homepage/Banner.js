import React from 'react'
import { Link } from 'react-router-dom'

function Banner() {
    return (
        <div className="container banner">
            <div className="row flex">
                <div className="col-lg-6 col-md-12">
                    <div className="heading">
                        <h2 className="display-4">Paying too much?</h2>
                    </div>
                    <p className="banner-description">PriceMatch throws the ball back into the consumer's court by helping compare prices for any item. Simply take a picture of the product and you get a list of stores and prices at your fingertips.</p>
                    <div className="buttons">
                        <Link to="/pricematch" type="button" className="btn btn-info">
                            Get Started!
                        </Link>
                        <button type="button" className="btn btn-outline-info">Learn More</button>
                    </div>
                </div>
                <div className="col-lg-6 col-md-12 banner-image">
                    <img src="./Banner.png" alt="Placeholder image" width="380" height="230"></img>
                </div>
            </div>
        </div>
    )
}

export default Banner
