import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import TableList from '../components/Table'
import getUsersVehicles from '../controller/Fahrzeuge'
import Button from 'react-bootstrap/Button'
import { NavLink } from "react-router-dom";

async function getData(){
  const vehicles = await getUsersVehicles()
  return vehicles
}

function Fahrzeuge() {
  if(verify()){
    return (
      <div className='Fahrzeuge'>
        <NavLink to="../Neuanmeldung">
        <Button variant='primary' style={{marginLeft: '50px', marginTop: '50px', marginBottom:'10px'}}>Neues Fahrzeug anmelden</Button>
        </NavLink>
        <Button variant='primary' style={{marginLeft: '10px', marginTop: '50px', marginBottom:'10px'}} disabled={!Array.isArray(getData())}>Fahrzeuge verwalten</Button>
        <TableList data={getData()} exception='Sie haben keine angemeldeten Fahrzeuge.' heads={['#', 'Marke', 'Modell', 'Erstzulassung', 'Hubraum', 'Kraftstoff', 'Emissionen', 'Nächste HU', 'Kennzeichen']}/>
      </div>
    )
  }
  return (
    <div className='Fahrzeuge'>
      <Infobox variant='danger' text='Sie müssen für diesen Bereich angemeldet sein.'/>
    </div>
  )
}

export default Fahrzeuge