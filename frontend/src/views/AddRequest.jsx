import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import { postRequest } from '../controller/Fuehrerschein'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import { useNavigate } from "react-router-dom"
import { useState } from 'react'


function AddRequest() {

  const navigate = useNavigate();

  const[verified, setVerified] = React.useState([])
  React.useEffect(() => setVerified(fetch_verified()), [])

  const fetch_verified = async () => {
    setVerified(await verify())
  }

  const [formData, setFormData] = useState({
    licenseclass: ""
  })

  const handleChange = (event) => {
    const name = event.target.name
    const value = event.target.value
    setFormData({...formData, [name]: value})
  }

  const onFormSubmit = (event) => {
    event.preventDefault()
    postRequest(formData)
    navigate("/Fuehrerschein")
  }

  if(verified){

    return (
      <div className='AddRequest'>
      <Form style={{margin: '50px'}} onSubmit={onFormSubmit}>
        <Form.Group controlId='class'>
            <Form.Control as="select" value={formData.licenseclass} name="licenseclass" onChange = { handleChange }>
              <option>Führerscheinklasse</option>
              <option value="AM">AM</option>
              <option value="A1">A1</option>
              <option value="A2">A2</option>
              <option value="A">A</option>
              <option value="B1">B1</option>
              <option value="B">B</option>
              <option value="C1">C1</option>
              <option value="C">C</option>
              <option value="D1">D1</option>
              <option value="D">D</option>
              <option value="BE">BE</option>
              <option value="C1E">C1E</option>
              <option value="CE">CE</option>
              <option value="D1E">D1E</option>
              <option value="DE">DE</option>
              <option value="L">L</option>
              <option value="T">T</option>
            </Form.Control>
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