import React from 'react'
import Navbar from './Homepage/Navbar'
import UploadImage from './price-matcher-page/UploadImage'
import Footer from './Homepage/Footer'
import Scroll from './Homepage/Scroll'
function PriceMatch() {
    return (
        <div>
            <Navbar />
            <UploadImage />
            <Footer />
            <Scroll showBelow={250} />
        </div>
    )
}

export default PriceMatch
