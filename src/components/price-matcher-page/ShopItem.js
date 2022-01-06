import React from 'react'

function ShopItem(props) {

    return(
        <div className="card text-white" style={{backgroundColor: '#000'}}>
            <div className="card-body">
                <h4 className="card-title text-white">{props.storeName}</h4>
                <p className="card-text text-white">{props.name}</p>
                <p className="card-text text-white">{props.price}</p>
                {/* <a href={data.url} class="btn btn-warning" target="_blank">Apply now</a> */}
            </div>
        </div>
    )
}

export default ShopItem