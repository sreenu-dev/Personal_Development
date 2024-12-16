function card(prop){
    return (
        <div className="card m-2" style={{ width: '18rem' }}>
            <img src={prop.imageURL} className="card-img-top" alt="Card image" />
            <div className="card-body">
                <h5 className="card-title">{prop.title}</h5>
                <p className="card-text">{prop.description}</p>
                {/* <a href="#" className="btn btn-primary">Go somewhere</a> */}
            </div>
        </div>
    )
}

export default card;