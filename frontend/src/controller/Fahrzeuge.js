import axios from 'axios'

export default async function getUsersVehicles(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'vehicle/user/'
    return await axios.get(URL, {withCredentials: true}).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}

export async function postVehicle(body){
    const URL = process.env.REACT_APP_BACKEND_URL + 'vehicle/create'
    return await axios.post(URL, body, {withCredentials: true})
}