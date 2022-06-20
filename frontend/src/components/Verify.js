import axios from 'axios'


export default async function verify(){
    const URL = process.env.REACT_APP_BACKEND_URL + 'auth'
    return await axios.get(URL, {withCredentials: true}).then(response =>{
        return response.data.auth
    })
}