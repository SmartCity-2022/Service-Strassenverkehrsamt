import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import TableList from '../components/Table'
import getUsersLicenses from '../controller/Fuehrerschein'
import Button from 'react-bootstrap/Button'
import { NavLink } from "react-router-dom";


async function getData(){
  const licenses = await getUsersLicenses()
  return licenses
}


function Fuehrerschein() {
  if(verify()){
    return (
      <div className='Fuehrerschein'>
        <NavLink to="../Fuehrerscheinanfrage">
        <Button variant='primary' style={{marginLeft: '50px', marginTop: '50px', marginBottom:'10px'}}>Führerschein Antrag erstellen</Button>
        </NavLink>
        <TableList data={getData()} exception='Sie haben keine Führerscheine oder Führerscheinanträge.' heads={['#', 'Klasse', 'Ausstellung']}/>
      </div>
    )
  }
  return (
    <div className='Fuehrerschein'>
      <Infobox variant='danger' text='Sie müssen für diesen Bereich angemeldet sein.'/>
    </div>
  )
}

export default Fuehrerschein