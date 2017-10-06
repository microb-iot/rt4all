var path = require('path');
var PythonShell = require('python-shell');
var script = "test2.py"

document.addEventListener('DOMContentLoaded', function() {
  var url = window.location.search.substr(1);
  var id = url.split("=")
  document.getElementById("machine_title").innerHTML = "Maquina " + id[1];
})

function put_data(id,data){
	document.getElementById(id).innerHTML = data;
}

function fill_data(){
	var nodeConsole = require('console');
	var myConsole = new nodeConsole.Console(process.stdout, process.stderr);
	var pyshell = new PythonShell(script,{pythonOptions: ['-u']});

	//Recogida de los mensajes de el script
	pyshell.on('message', function (message) {
		myConsole.log(message);
		put_data("pressure_sensor_1",message.toString());
	});

	//Termina el proceso python
	pyshell.end(function (err) {
		if (err){
	    	throw err;
		};
		add_options("selector",machines_list);
		myConsole.log('finished');
  	});
}