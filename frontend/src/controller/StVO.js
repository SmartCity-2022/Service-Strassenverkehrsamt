import axios from 'axios'

export async function getUsersPenaltys(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'penalty/user/'
    return await axios.get(URL, {withCredentials: true}).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}

export async function getUsersBills(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'bill/user/'
    return await axios.get(URL, {withCredentials: true}).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}