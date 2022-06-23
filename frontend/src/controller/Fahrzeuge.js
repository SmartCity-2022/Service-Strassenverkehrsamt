import axios from 'axios'

export async function getUsersVehicles(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'vehicle/user/'
    return await axios.get(URL, {withCredentials: true}).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}

export async function getUsersRegisterRequests(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'registerrequest/user/'
    return await axios.get(URL, {withCredentials: true}).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}

export async function postVehicle(body){
    const URL = process.env.REACT_APP_BACKEND_URL + 'vehicle/create'
    const response = await axios.post(URL, body, {withCredentials: true})
    const URL_REG = process.env.REACT_APP_BACKEND_URL + 'registerrequest/create'
    return await axios.post(URL_REG, {"vehicle": response.data.id}, {withCredentials: true})
}