
import './App.css';
import Component1 from './Component1';
function getDate(date){
  return date.toLocaleDateString()+" "+ date.toLocaleTimeString()
}
function App() {
  let nome="Leandro"
  return (
    <div className="App">
      <Component1>Pazienza</Component1>
      <Component1>Leandro</Component1>
      <Component1>Adriano</Component1>
      <h1>Prima App React di {nome}{/*comment*/}</h1>
      <h2>
        {
          new Date().toLocaleDateString()+" "+ new Date().toLocaleDateString()
        }
        </h2>
          <h2>{getDate(new Date())}</h2>
    </div>
  );
}

export default App;
