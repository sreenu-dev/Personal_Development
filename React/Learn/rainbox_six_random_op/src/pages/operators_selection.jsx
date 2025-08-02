import { useState } from "react";

export default function OperatorSelection() {
    let attackers = [
        { name: "Sledge", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6eIdbZWLBIdtCygNAu9uue/8856e29f0e9ebc3b6ed996223586ebce/r6-operators-list-sledge.png" },
        { name: "Thatcher", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5QGPM6l25ybaINnaIaLgvm/d018abc75d44758d666ad6bea0a38a9b/r6-operators-list-thatcher.png" },
        { name: "Ash", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/QOEBDfqjtUxVBc31l8L9f/4d9b112565baf81d56d69279b95cd463/r6-operators-list-ash_317253.png" },
        { name: "Thermite", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3NQW8lJVslVSaYSiBlAleU/09fd8e3e946f2e71f39182b9ff18dd77/r6-operators-list-thermite.png" },
        { name: "Twitch", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/Z9R1Anc8MHwbG5iyPoOf2/69fe9aee30e03322a4e09d4b87de15aa/r6-operators-list-twitch.png" },
        { name: "Montagne", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1hxlGxmToB93urkgbIzUvW/fa894cd6ab38358284a3a1858cabbeee/r6-operators-list-montagne.png" },
        { name: "Glaz", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6R6uQlUmkh7KYoFYeeGpvj/fb92cfe1a0501d63a0ffa417c004e84e/r6-operators-list-glaz.png" },
        { name: "Fuze", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/BsiNYFp7htro1mOEgiKf1/eef48a78d9a7c1cb2dcac07e1d06edb1/r6-operators-list-fuze.png" },
        { name: "Blitz", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4NZvCtXwtcCq1s65H7mK5y/8d70872df8319e1d162a31bbf404ed2c/r6-operators-list-blitz.png" },
        { name: "IQ", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3lP88YKPk0boUyisZD0LT7/6b3ef86531c459ef9e573f056d6eddf5/r6-operators-list-iq.png" },
        { name: "Buck", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3k68pZu62GPbCAFOSCej9a/3c3d3da1f7109a396fb59dcf06c5c4c8/r6-operators-list-buck.png" },
        { name: "Blackbeard", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5u6Ak7dkTb4yOjaP1hlGuT/cf52b8e0ac096bf55d764fc8b4fe7f9b/r6s-operators-list-blackbeard.png" },
        { name: "CAPITÃO", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3AZlhNFA21aKL2MdAIEwa8/abfce9018a7a08c120d707fbc28ae709/r6-operators-list-capitao.png" },
        { name: "Hibana", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/7mAs4mz2zA4wjPZsNg6tys/e4fbdbfe20406c2655b56ba420b839aa/r6-operators-list-hibana.png" },
        { name: "Jackal", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/kbyJly2JDRxFrjFSrptiy/ebbdae24cdfed025b0872742bb6c2a96/r6-operators-list-jackal.png" },
        { name: "Zofia", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/z60t1OJxJoHqm2zp0t5dL/4acc0904444f43b12a17f6a578322cf9/r6-operators-list-zofia.png" },
        { name: "Dokkaebi", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/7fjUupLXClpcdTyqdvPv24/e4492917c18682ef09f9b0445176b2f2/r6-operators-list-dokkaebi.png" },
        { name: "Lion", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4wYSIOO4AKq0nw1GbulGns/fcd32bda72facd7062a25ad3764f21e9/r6-operators-list-lion.png" },
        { name: "Finka", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6VkZ60XV4HWhbQaoMpfjnw/1bd7667a572622371627e90e5e572455/r6-operators-list-finka.png" },
        { name: "Maverick", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1MmaEupq7KOe6it1trqIWP/3f4246349a36e28f4d9299f9368612c1/r6-operators-list-maverick.png" },
        { name: "Gridlock", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/27gUsHtPmP86NRs4cPug1o/31ea0005ad1afc68a8ebcc477934ded6/r6-operators-list-gridlock.png" },
        { name: "NØKK", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/VeXso9iKMqBDrSmuJ2kBx/b8020ed099ddbdcb31ec809b9d7da152/r6-operators-list-nokk.png" },
        { name: "Kali", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/41NACeIbkdnIWgnwq0HzD4/9713f8e58b9a8c253b7507b59169bb3c/r6-operators-list-kali_358317.png" },
        { name: "Iana", image: "https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6vES8lEllMwW9OaBYRT7YX/39b5fe90684d7ce637a7d025cdd1ec96/r6s-operator-list-iana.png" }
    ]
    let randomAttacker = attackers[Math.floor(Math.random() * attackers.length)];
    let [getRandomAttacker,setRandomAttacker]= useState(randomAttacker);


    function getRandomAttackerFun() {
        randomAttacker = attackers[Math.floor(Math.random() * attackers.length)];
        setRandomAttacker(randomAttacker);
        console.log(randomAttacker);
    }

    return (
        <div>
            Hai Operator Selection Page comes here
            <div className="d-flex">
                <div class="h2">Attackers</div>
                <div className="ps-3">
                    <button className="btn btn-primary" onClick={getRandomAttackerFun}>Get Random Attacker</button>
                </div>
            </div>
            <div>
                <div className="d-flex flex-column align-items-center border border-black m-2 p-2">
                    <span>{randomAttacker.name}</span>
                    <img src={randomAttacker.image} />
                </div>
            </div>
            {/* <div className="d-flex flex-wrap">
                {attackers.map((attacker, index) => (
                    <div className="d-flex flex-column align-items-center border border-black m-2 p-2" key={index}>
                        <span>{attacker.name}</span>
                        <img src={attacker.image} />
                    </div>
                ))}

            </div> */}
        </div>
    )
}