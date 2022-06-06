import React from "react";
import Table from 'react-bootstrap/Table'
import Infobox from "./Infobox";

export default function TableList(props){
    if(!Array.isArray(props.data)){
        return (
            <Infobox variant='info' text={props.exception}/>
        )
    }
    return(
        <Table>
            <thead>
                {
                    props.heads.map(head =>(
                        <th>{head}</th>
                    ))
                }
            </thead>
            <tbody>
                {
                    props.data.map(set =>(
                        <tr>
                            {
                                set.map(row =>(
                                    <td>{ row }</td>
                                ))
                            }
                        </tr>
                    ))
                }
            </tbody>
        </Table>
    )
}