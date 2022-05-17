import React from "react";
import ItemCard from '../components/ItemCard'

const divStyle = {
  display: 'flex',
  align: 'center',
  alignItems: 'center',
  border: '10px',
  'justify-content': 'center'
};

function Home() {
  return (
    <div className="home" style={divStyle}>
        <ItemCard title="Fahrzeuge verwalten" description="Verwalten Sie Ihre Fahrzeuge oder melden Sie neue an." target="./Fahrzeuge" img={ require("../assets/car.png") }/>
        <ItemCard title="Führerscheinstelle" description="Verwalten Sie Führerschein Anträge." target="./Fuehrerschein" img={ require("../assets/license.png") }/>
        <ItemCard title="StVO" description="Sehen Sie Ihre Vergehen im Straßenverkehr ein." target="./StVO" img={ require("../assets/stvo.png") }/>
    </div>
  );
}

export default Home;