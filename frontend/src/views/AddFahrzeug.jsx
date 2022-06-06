import React from 'react'
import verify from '../components/Verify'
import Infobox from '../components/Infobox'
import Form from 'react-bootstrap/Form'
import TableList from '../components/Table'
import getUsersVehicles from '../controller/Fahrzeuge'
import Button from 'react-bootstrap/Button'

function AddFahrzeug() {
  if(verify()){
    return (
      <div className='AddFahrzeug'>
          <Form style={{margin: '50px'}}>
            <Form.Group controlId='brand'>
              <Form.Label>Marke</Form.Label>
              <Form.Control type="text" placeholder="Marke des Fahrzeugs"/>
            </Form.Group>
            <Form.Group controlId='model'>
              <Form.Label>Modell</Form.Label>
              <Form.Control type="text" placeholder="Fahrzeugmodell"/>
            </Form.Group>
            <Form.Group controlId='firstregistration'>
              <Form.Label>Erstzulassung</Form.Label>
              <Form.Control type="date"/>
            </Form.Group>
            <Form.Group controlId='displacement'>
              <Form.Label>Hubraum in cm3</Form.Label>
              <Form.Control type="number" placeholder="2000"/>
            </Form.Group>
            <Form.Group controlId='fueltype'>
              <Form.Label> Kraftstoffart</Form.Label>
              <Form.Select aria-label="fueltype" controlId='fueltype'>
                <option>Kraftstoffart des Fahrzeuges</option>
                <option value="1">Benzin</option>
                <option value="2">Diesel</option>
                <option value="3">Sonstige</option>
              </Form.Select>
            </Form.Group>
            <Form.Group controlId='emissions'>
              <Form.Label>Abgase / 100km </Form.Label>
              <Form.Control type="number" placeholder="100"/>
            </Form.Group>
            <Form.Group controlId='licenseplate'>
              <Form.Label>Wunschkennzeichen</Form.Label>
              <Form.Control type="text" placeholder="MI:MI:1234"/>
            </Form.Group>
            <Form.Group controlId='hucertificate'>
              <Form.Label>TüV Bescheinigung</Form.Label>
              <Form.Control type="file"/>
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