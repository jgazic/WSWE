/**
 * Pridobi podatke iz obrazca in jih vrne v obliki JSON objekta.
 * @param  {HTMLFormControlsCollection} elements  Elementi obrazca
 * @return {Object}                               Object literal
 */
const formToJSON = elements => [].reduce.call(elements, (data, element) => 
{
	if(element.name!="")
	{
		data[element.name] = element.value;
	}
  return data;
}, {});


function read_id()
{
var urlParams = new URLSearchParams(window.location.search);

polje_id=document.getElementById('lunch_id')
polje_id.value = urlParams.get('id')
console.log(urlParams.get('id'))
polje_id2=document.getElementById('lunch_id2')
polje_id2.value = urlParams.get('id')
console.log(urlParams.get('id'))
}


function suggest()
{
	
	const data = formToJSON(document.getElementById("obrazec").elements);	
	var JSONdata = JSON.stringify(data, null, "  ");						
	
	var myHeaders = new Headers();
	myHeaders.append("Content-Type", "application/json");

	var raw = JSON.stringify(data);

	var requestOptions = {
	method: 'POST',
	headers: myHeaders,
	body: raw,
	redirect: 'follow'
	};



	fetch("http://localhost:5000/suggestions", requestOptions)
	.then(response => response.json())
	.then(json => {
		odgovor = json.status
		})	
	.then(polje=document.getElementById('odgovor'))
	.then(polje.innerHTML = "")
	.then(data => polje.innerHTML =  odgovor)
	
	
	.catch(error => console.log('error', error));
}
	 	
function decide()
{
	
	const data = formToJSON(document.getElementById("wswe").elements);	
	var JSONdata = JSON.stringify(data, null, "  ");						
	
	var myHeaders = new Headers();
	myHeaders.append("Content-Type", "application/json");

	var raw = JSON.stringify(data);

	var requestOptions = {
	method: 'POST',
	headers: myHeaders,
	body: raw,
	redirect: 'follow'
	};



	fetch("http://localhost:5000/wswe", requestOptions)
	.then(response => response.json())
	.then(json => {
		odlocitev = json.decision,
		ime = json.name
		})	
	.then(polje=document.getElementById('decision'))
	.then(polje.innerHTML = "")
	.then(data => polje.innerHTML = 'Final decision: ' + odlocitev + '<br>' + 'Suggested by: ' +ime)

	.catch(error => console.log('error', error));
}