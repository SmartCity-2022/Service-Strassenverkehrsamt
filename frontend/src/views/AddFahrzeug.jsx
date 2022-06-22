import { useState } from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import Form from 'react-bootstrap/Form'
import { postVehicle } from '../controller/Fahrzeuge'
import Button from 'react-bootstrap/Button'
import React from 'react'
import { useNavigate } from "react-router-dom"

function AddFahrzeug() {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    brand: "",
    model: "",
    firstregistration: "",
    displacement: 0,
    fueltype: "",
    emissions: 0,
    licenseplate: ""
  })

  const handleChange = (event) => {
    const name = event.target.name
    const value = event.target.value
    setFormData({...formData, [name]: value})
  }

  const onFormSubmit = (event) => {
    event.preventDefault()
    postVehicle(formData)
    navigate("/Fahrzeuge")
  }

  const[verified, setVerified] = React.useState([])
  React.useEffect(() => setVerified(fetch_verified()), [])

  const fetch_verified = async () => {
    setVerified(await verify())
  }

  if(verified === true){

    return (
      <div className='AddFahrzeug'>
          <Form style={{margin: '50px'}} onSubmit={onFormSubmit}>
            <Form.Group name='brand'>
              <Form.Label>Marke</Form.Label>
              <Form.Control type="text" placeholder="Marke des Fahrzeugs" value={formData.brand} name="brand" onChange = { handleChange }/>
            </Form.Group>
            <Form.Group name='model'>
              <Form.Label>Modell</Form.Label>
              <Form.Control type="text" placeholder="Fahrzeugmodell" value={formData.model} name="model" onChange = { handleChange }/>
            </Form.Group>
            <Form.Group name='firstregistration'>
              <Form.Label>Erstzulassung</Form.Label>
              <Form.Control type="date" name="firstregistration" value={formData.firstregistration} onChange = { handleChange }/>
            </Form.Group>
            <Form.Group name='displacement'>
              <Form.Label>Hubraum in cm3</Form.Label>
              <Form.Control type="number" placeholder="2000" value={formData.displacement} name="displacement" onChange = { handleChange }/>
            </Form.Group>
            <Form.Group name='fueltype'>
              <Form.Label> Kraftstoffart</Form.Label>
              <Form.Control as="select" value={formData.fueltype} name="fueltype" onChange = { handleChange }>
                <option>Kraftstoffart des Fahrzeuges</option>
                <option value="Benzin">Benzin</option>
                <option value="Diesel">Diesel</option>
                <option value="Sonstige">Sonstige</option>
              </Form.Control>
            </Form.Group>
            <Form.Group name='emissions'>
              <Form.Label>Abgase / 100km </Form.Label>
              <Form.Control type="number" placeholder="100" name="emissions" value={formData.emissions} onChange = { handleChange }/>
            </Form.Group>
            <Form.Group name='licenseplate'>
              <Form.Label>Wunschkennzeichen</Form.Label>
              <Form.Control type="text" placeholder="MI:MI:1234" name="licenseplate" value={formData.licenseplate} onChange = { handleChange }/>
            </Form.Group>
            <Form.Group name='registration1' className="mb-3">
              <Form.Label>Fahrzeugbrief</Form.Label>
              <Form.Control type="file" onChange = { handleChange }/>
            </Form.Group>
            <Form.Group name='registration2' className="mb-3">
              <Form.Label>Fahrzeugschein</Form.Label>
              <Form.Control type="file" onChange = { handleChange }/>
            </Form.Group>
            <Form.Group name='hucertificate' className="mb-3">
              <Form.Label>TüV Bescheinigung</Form.Label>
              <Form.Control type="file" onChange = { handleChange }/>
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
    <div className='AddFahrzeug'>
      <Infobox variant='danger' text='Sie müssen für diesen Bereich angemeldet sein.'/>
    </div>
  )
}

export default AddFahrzeug