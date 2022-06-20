import axios from 'axios'

export async function getUsersLicenses(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'license/user/'
    return await axios.get(URL, {withCredentials: true}).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}

export async function getUsersLicenseRequests(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'licenserequest/user/'
    return await axios.get(URL, {withCredentials: true}).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}

export async function postRequest(body){
    const URL = process.env.REACT_APP_BACKEND_URL + 'licenserequest/create'
    return await axios.post(URL, body, {withCredentials: true})
}