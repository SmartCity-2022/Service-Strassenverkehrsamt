import React from 'react'
import Alert from 'react-bootstrap/Alert'

export default function Infobox(props){
    return(
        <Alert variant={props.variant} style={{marginLeft: '50px', marginRight: '50px'}}>
            {props.text}
        </Alert>
    )
}