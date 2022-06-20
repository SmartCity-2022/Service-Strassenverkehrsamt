import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import TableList from '../components/Table'
import getUsersPenaltys from '../controller/StVO'


function StVO() {
  const [data, setData] = React.useState([])
  React.useEffect(() => { fetch_vehicles() }, [])

  const fetch_vehicles = async () => {
      setData(await getUsersPenaltys())
  }
  
  const[verified, setVerified] = React.useState([])
  React.useEffect(() => setVerified(fetch_verified()), [])

  const fetch_verified = async () => {
    setVerified(await verify())
  }

  if(verified){

    return (
      <div className='StVO'>
        <TableList style={{marginTop: '60px'}} data={data} exception='Sie sind nicht im Straßenverkehr aufgefallen.' heads={['#', 'Ausstellung', 'Strafe', 'Beschreibung']}/>
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