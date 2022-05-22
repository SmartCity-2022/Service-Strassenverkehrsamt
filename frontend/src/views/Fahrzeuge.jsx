import React from 'react'

function test(){
  var token = localStorage.getItem("token")
  if(token){
    return "YES"
  }
  return "NO"
}

function Fahrzeuge() {
  return (
    <div className='Fahrzeuge'>
      {test()}
    </div>
  )
}

export default Fahrzeuge