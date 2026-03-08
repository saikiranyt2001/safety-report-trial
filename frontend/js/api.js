async function generateReport(){

const company = document.getElementById("company").value
const description = document.getElementById("description").value

const response = await fetch("http://127.0.0.1:8000/generate-report",{

method:"POST",
headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
company:company,
description:description
})

})

const data = await response.json()

document.getElementById("result").innerText = data.report

}
