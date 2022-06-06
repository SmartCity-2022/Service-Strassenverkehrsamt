import axios from 'axios'

export default async function getUsersPenaltys(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'penalty'
    axios.get(URL).then(response =>{
        const isResponse = response.data && response.data.length
        return isResponse ? response.data : []
    })
}