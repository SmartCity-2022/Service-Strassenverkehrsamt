import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import TableList from '../components/Table'
import {getUsersLicenses, getUsersLicenseRequests} from '../controller/Fuehrerschein'
import Button from 'react-bootstrap/Button'
import { NavLink } from "react-router-dom";
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'


function Fuehrerschein() {
  const [licenses, setLicenses] = React.useState([])
  React.useEffect(() => { fetch_licenses() }, [])

  const fetch_licenses = async () => {
      setLicenses(await getUsersLicenses())
  }
  
  const [requests, setRequests] = React.useState([])
  React.useEffect(() => { fetch_requests() }, [])

  const fetch_requests = async () => {
      setRequests(await getUsersLicenseRequests())
  }
  
  const[verified, setVerified] = React.useState([])
  React.useEffect(() => setVerified(fetch_verified()), [])

  const fetch_verified = async () => {
    setVerified(await verify())
  }

  if(verified === true){

    return (
      <div className='Fuehrerschein'>
        <NavLink to="../Fuehrerscheinanfrage">
        <Button variant='primary' style={{marginLeft: '50px', marginTop: '50px', marginBottom:'10px'}}>Führerschein Antrag erstellen</Button>
        </NavLink>
        <Tabs defaultActiveKey="licenses" id="tabs" className="mb-3">
          <Tab eventKey="licenses" title="Führerscheine">
            <Infobox variant='light' text='Sehen Sie hier Ihre anerkannten Führerscheine an.'/>
            <TableList data={licenses} exception='Sie haben keine Führerscheine.'/>
          </Tab>
          <Tab eventKey="requests" title="Führerschein Anträge">
            <Infobox variant='light' text='Sehen Sie hier Ihre offenen Führerscheinanträge an.'/>
            <TableList data={requests} exception='Sie haben keine offenen Führerscheinanträge.'/>
          </Tab>
        </Tabs>
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