import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import TableList from '../components/Table'
import getUsersPenaltys from '../controller/StVO'


async function getData(){
  const penaltys = await getUsersPenaltys()
  return penaltys
}


function StVO() {
  if(verify()){
    return (
      <div className='StVO'>
        <TableList style={{marginTop: '60px'}} data={getData()} exception='Sie sind nicht im Straßenverkehr aufgefallen.' heads={['#', 'Ausstellung', 'Strafe', 'Beschreibung']}/>
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