import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import { useNavigate } from "react-router-dom"


function AddRequest() {

  const navigate = useNavigate();

  const[verified, setVerified] = React.useState([])
  React.useEffect(() => setVerified(fetch_verified()), [])

  const fetch_verified = async () => {
    setVerified(await verify())
  }

  if(verified){

    return (
      <div className='AddRequest'>
      <Form style={{margin: '50px'}}>
        <Form.Group controlId='class'>
            <Form.Select aria-label="class" controlId='class'>
              <option>Führerscheinklasse</option>
              <option value="1">AM</option>
              <option value="2">A1</option>
              <option value="3">A2</option>
              <option value="4">A</option>
              <option value="5">B1</option>
              <option value="6">B</option>
              <option value="7">C1</option>
              <option value="8">C</option>
              <option value="9">D1</option>
              <option value="10">D</option>
              <option value="11">BE</option>
              <option value="12">C1E</option>
              <option value="13">CE</option>
              <option value="14">D1E</option>
              <option value="15">DE</option>
              <option value="16">L</option>
              <option value="17">T</option>
            </Form.Select>
        </Form.Group>
        <Form.Group>
          <Button variant="primary" type="submit" style={{marginTop: '15px'}}>
            Antrag erstellen
          </Button>
        </Form.Group>
      </Form>
      </div>
    )
  }
  return (
    <div className='AddRequest'>
      <Infobox variant='danger' text='Sie müssen für diesen Bereich angemeldet sein.'/>
    </div>
  )
}

export default AddRequest