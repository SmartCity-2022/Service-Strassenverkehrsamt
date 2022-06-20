import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import TableList from '../components/Table'
import {getUsersPenaltys, getUsersBills} from '../controller/StVO'
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'


function StVO() {
  const [penaltys, setPenaltys] = React.useState([])
  React.useEffect(() => { fetch_penaltys() }, [])

  const fetch_penaltys = async () => {
      setPenaltys(await getUsersPenaltys())
  }
  
  const [bills, setBills] = React.useState([])
  React.useEffect(() => { fetch_bills() }, [])

  const fetch_bills= async () => {
      setBills(await getUsersBills())
  }

  const[verified, setVerified] = React.useState([])
  React.useEffect(() => setVerified(fetch_verified()), [])

  const fetch_verified = async () => {
    setVerified(await verify())
  }

  if(verified){

    return (
      <div className='StVO'>
      <Tabs defaultActiveKey="penaltys" id="tabs" className="mb-3">
        <Tab eventKey="penaltys" title="Straftaten">
          <TableList style={{marginTop: '60px'}} data={penaltys} exception='Sie sind nicht im Straßenverkehr aufgefallen.'/>
        </Tab>
        <Tab eventKey="bills" title="Rechnungen">
          <TableList style={{marginTop: '60px'}} data={bills} exception='Sie haben keine Rechnungen beim Straßenverkehrsamt.'/>
        </Tab>
      </Tabs>
      </div>
    )
  }
  return (
    <div className='StVO'>
      <Infobox variant='danger' text='Sie müssen für diesen Bereich angemeldet sein.'/>
    </div>
  )
}

export default StVO