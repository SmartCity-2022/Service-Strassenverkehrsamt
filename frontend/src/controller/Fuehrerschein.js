import axios from 'axios'

export default async function getUsersLicenses(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'license/user/'
    return await axios.get(URL, {withCredentials: true}).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}

export async function postVehicle(body){
    const URL = process.env.REACT_APP_BACKEND_URL + 'license/create'
    return await axios.post(URL, body, {withCredentials: true})
}