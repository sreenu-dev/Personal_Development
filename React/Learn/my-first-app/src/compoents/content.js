import FirstButton from './button';
import card from './card';
import Card from './card'
import Counter from './counter'
import InputForm from './inputForm'
import ShowHideExample from './showHideExample';
import React, { useState } from 'react';
import TodoApp from './todoApp';

/**
 * Render content for first app
 * @param {string} name 
 * @param {number} age 
 * @returns {JSX.Element}
 */

const cardData = [
    { cardTitle: "Card 1", cardDescription: "This is card 1", cardImageURL: "https://fastly.picsum.photos/id/808/200/200.jpg?hmac=OeCbxYuUpLdh3AWFCaO6QKu8PmNGdmBZbVOnx7Pdflk" },
    { cardTitle: "Card 2", cardDescription: "This is card 2", cardImageURL: "https://fastly.picsum.photos/id/906/200/200.jpg?hmac=jQ-m5xgglMRMPvZhK3539qEkxPG1FVUae6AeV_HKQfg" },
    { cardTitle: "Card 3", cardDescription: "This is card 3", cardImageURL: "https://fastly.picsum.photos/id/259/200/200.jpg?hmac=F9blvALDAoKm-lOnYw9g0q_RC51-6K1Msawm_dQzhIs" },
    { cardTitle: "Card 4", cardDescription: "This is card 4", cardImageURL: "https://fastly.picsum.photos/id/387/200/200.jpg?hmac=xAsfqp-sKuFi5HUw3VKwBRqzmG_uqFbmk3oiHTJXjq4" },
    { cardTitle: "Card 5", cardDescription: "This is card 5", cardImageURL: "https://fastly.picsum.photos/id/889/200/200.jpg?hmac=mzo0mKfXHC9qb2dLw47jTrXZmlF9g6c6EuUFOWz0T5U" },
]
function Content(prop) {

    const [toggleView, setToggleView] = useState(false);

    return (
        <div>
            <input type='checkbox' onChange={()=>setToggleView(!toggleView)}></input>
            {toggleView && <div>
                <div>
                    <p>This is my first app in React</p>
                    <Counter></Counter>
                    <InputForm></InputForm>
                    <ShowHideExample></ShowHideExample>
                    <div>
                        <p>
                            <span>Name: {prop.name}</span><br></br>
                            <span>Age: {prop.age}</span><br></br>
                            <FirstButton buttonText="Click Me"></FirstButton>
                            <FirstButton buttonText="Click Me Too"></FirstButton>
                            <FirstButton buttonText="Click Me Three"></FirstButton>

                        </p>
                    </div>

                    <div className="container d-flex flex-wrap">
                        {cardData.map((cardData, index) => {
                            return <Card key={index} title={cardData.cardTitle} description={cardData.cardDescription} imageURL={cardData.cardImageURL}></Card>
                        })}
                    </div>
                </div>
            </div>}

            {!toggleView && <div>
                    <TodoApp></TodoApp>
                </div>}
        </div>
    );
}

export default Content;