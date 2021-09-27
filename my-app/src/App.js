import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react';
import {Deploy} from './Component/Deploy/Deploy';

function App() {
  const [state, setState] = useState({})
  
  // a blank [] means that it will only run once upon load
  useEffect(() => {
    fetch('/api').then(response => {
      if(response.status == 200) {
        return response.json()
      }
    }).then(data => setState(data))
    .then(error => console.log(error))
  },[])

  return (
    <div className="App">
      <Deploy prop={state}/>
    </div>
  );
}

export default App;
