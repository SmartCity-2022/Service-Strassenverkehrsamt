import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import TableList from '../components/Table'
import {getUsersVehicles, getUsersRegisterRequests} from '../controller/Fahrzeuge'
import Button from 'react-bootstrap/Button'
import { NavLink } from "react-router-dom"
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'

function Fahrzeuge() {

  const [vehicles, setVehicles] = React.useState([])
  React.useEffect(() => { fetch_vehicles() }, [])

  const fetch_vehicles = async () => {
      setVehicles(await getUsersVehicles())
  }

  const [v_requests, setV_requests] = React.useState([])
  React.useEffect(() => { fetch_v_requests() }, [])

  const fetch_v_requests = async () => {
      setV_requests(await getUsersRegisterRequests())
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
        <Button variant='primary' style={{marginLeft: '10px', marginTop: '50px', marginBottom:'10px'}} disabled={!Array.isArray(vehicles)}>Fahrzeuge verwalten</Button>
        <Tabs defaultActiveKey="kfz" id="tabs" className="mb-3">
          <Tab eventKey="kfz" title="Angemeldete Fahrzeuge">
            <Infobox variant='light' text='Sehen Sie hier Ihre angemeldeten Fahrzeuge an.'/>
            <TableList data={vehicles} exception='Sie haben keine angemeldeten Fahrzeuge.'/>
          </Tab>
          <Tab eventKey="req" title="Registrierungs Anträge">
            <Infobox variant='light' text='Sehen Sie hier Ihre offenen Registrierungsanträge an.'/>
            <TableList data={v_requests} exception='Sie haben keine offenen Anträge.'/>
          </Tab>
        </Tabs>
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