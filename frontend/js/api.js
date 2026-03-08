const API_URL = "http://localhost:8000";

async function generateReport(data){
	const response = await fetch(API_URL + "/generate-report",{
		method:"POST",
		headers:{
			"Content-Type":"application/json"
		},
		body:JSON.stringify(data)
	});
	return await response.json();
}

document.getElementById("result").innerText = data.report

}
