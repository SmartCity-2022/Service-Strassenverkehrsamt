import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import TableList from '../components/Table'
import getUsersVehicles from '../controller/Fahrzeuge'
import Button from 'react-bootstrap/Button'
import { NavLink } from "react-router-dom"

function Fahrzeuge() {

  const [data, setData] = React.useState([])
  React.useEffect(() => { fetch_vehicles() }, [])

  const fetch_vehicles = async () => {
      setData(await getUsersVehicles())
  }

  const[verified, setVerified] = React.useState([])
  React.useEffect(() => setVerified(fetch_verified()), [])

  const fetch_verified = async () => {
    setVerified(await verify())
  }

  if(verified){

    return (
      <div className='Fahrzeuge'>
        <NavLink to="../Neuanmeldung">
        <Button variant='primary' style={{marginLeft: '50px', marginTop: '50px', marginBottom:'10px'}}>Neues Fahrzeug anmelden</Button>
        </NavLink>
        <Button variant='primary' style={{marginLeft: '10px', marginTop: '50px', marginBottom:'10px'}} disabled={!Array.isArray(data)}>Fahrzeuge verwalten</Button>
        <TableList data={data} exception='Sie haben keine angemeldeten Fahrzeuge.'/>
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