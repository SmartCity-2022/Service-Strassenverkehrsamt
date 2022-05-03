import './App.css';
import axios from 'axios';
import {useState, useEffect} from 'react'

function App() {

  const [bill, setBill] = useState([]); 
  const getBill = () => {
    axios.get("http://127.0.0.1:8000/bill") 
      .then((response) => {
        console.log(response);
        const myBill = response.data;
        setBill(myBill);
      });
  };

  useEffect(() => getBill(), []);

  return (
    <div className="App">
      {
        bill.map((bills)=>(
          <>
            <span>
              {bills.id}
            </span>
            <span>
              {bills.value}
            </span>
            <span>
              {bills.description}
            </span>
            <span>
              {bills.issued}
            </span>
            <span>
              {bills.payed}
            </span>
            <span>
              {bills.receiver}
            </span>
            <span>
              {bills.deadline}
            </span>
          </>
        ))
      }
    </div>
  );
}

export default App;
