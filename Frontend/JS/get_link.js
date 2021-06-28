/**
 * Pridobi podatke iz obrazca in jih vrne v obliki JSON objekta.
 * @param  {HTMLFormControlsCollection} elements  Elementi obrazca
 * @return {Object}                               Object literal
 */


function get_id()
{
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
      method: 'GET',
      headers: myHeaders,

      redirect: 'follow'
    };
    
    fetch("http://localhost:5000/wswe", requestOptions)
      .then(response => response.json())
      .then(polje=document.getElementById('link'))
      .then(polje.innerHTML = "")
      .then(result => polje.innerHTML +="<a href='"+result+"'>'"+result+"'</a>")
      

      .catch(error => console.log('error', error));
}

