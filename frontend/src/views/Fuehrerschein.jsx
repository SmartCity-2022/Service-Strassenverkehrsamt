import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import TableList from '../components/Table'
import getUsersLicenses from '../controller/Fuehrerschein'
import Button from 'react-bootstrap/Button'
import { NavLink } from "react-router-dom";


function Fuehrerschein() {
  const [data, setData] = React.useState([])
  React.useEffect(() => { fetch_vehicles() }, [])

  const fetch_vehicles = async () => {
      setData(await getUsersLicenses())
  }
  
  const[verified, setVerified] = React.useState([])
  React.useEffect(() => setVerified(fetch_verified()), [])

  const fetch_verified = async () => {
    setVerified(await verify())
  }

  if(verified){

    return (
      <div className='Fuehrerschein'>
        <NavLink to="../Fuehrerscheinanfrage">
        <Button variant='primary' style={{marginLeft: '50px', marginTop: '50px', marginBottom:'10px'}}>Führerschein Antrag erstellen</Button>
        </NavLink>
        <TableList data={data} exception='Sie haben keine Führerscheine oder Führerscheinanträge.' heads={['#', 'Klasse', 'Ausstellung']}/>
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