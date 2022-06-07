import axios from 'axios'

export default async function getUsersVehicles(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'vehicle'
    axios.get(URL).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}