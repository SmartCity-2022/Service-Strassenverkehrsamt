import React from "react";
import Table from 'react-bootstrap/Table'
import Infobox from "./Infobox";


export default function TableList(props){
    if(props.data.length <= 0){
        return (
            <Infobox variant='info' text={props.exception}/>
        )
    }
    return(
        <Table>
            <thead>
                <tr>
                    {
                        Object.entries(props.data[0]).map(
                            ([key, value]) => <th key={key}>{key}</th>
                        )
                    }
                </tr>
            </thead>
            <tbody>
                {
                    props.data.map((set) =>(
                        <tr key={set.id}>
                            {
                                Object.entries(set).map(
                                    ([key, value]) => <td>{value}</td>
                                )
                            }
                        </tr>
                    ))
                }
            </tbody>
        </Table>
    )
}