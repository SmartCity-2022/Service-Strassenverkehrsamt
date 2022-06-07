import React from 'react'
import { Card } from 'react-bootstrap'
import { NavLink } from "react-router-dom";


export default function ItemCard(props) {
  return (
      <Card style={{ width: '18rem', margin: '10px'}}>
        <NavLink className="nav-link" to={props.target}>
        <Card.Img variant="top" src={props.img} width="200px" height="150px"/>
          <Card.Body>
            <Card.Title>{props.title}</Card.Title>
            <Card.Text>{props.description}</Card.Text>
          </Card.Body>
        </NavLink>
      </Card>
  )
}
