var path = require('path');
var PythonShell = require('python-shell');

var nodeConsole = require('console');
var myConsole = new nodeConsole.Console(process.stdout, process.stderr);

var exec = require('child_process').exec;
var stream;

var key_list = ["w","a","s","d"];

//DOM functions

document.addEventListener('DOMContentLoaded', function() {
  var url = window.location.search.substr(1);
  var id = url.split("=")
  document.getElementById("machine_title").innerHTML = "Maquina " + id[1];
})

document.onkeypress = function(evt) {
    evt = evt || window.event;
    var charCode = evt.keyCode || evt.which;
    var key_pressed = String.fromCharCode(charCode);

    if(key_list.indexOf(key_pressed) != -1){
   		send_key_pressed(key_pressed);
   	}
}

//Fill data functions

function put_data(id,data){
	document.getElementById(id).innerHTML = data;
}

function fill_data(){
	var pyshell = new PythonShell("test2.py",{pythonOptions: ['-u']});

	//Recogida de los mensajes de el script
	pyshell.on('message', function (message) {
		//myConsole.log(message);
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

//Send data functions

function send_key_pressed(key_pressed){
	var pyshell_send = new PythonShell('test3.py');
	pyshell_send.send("Tecla pulsada: " + key_pressed);

	pyshell_send.on('message', function (message) {
  		//Receive "print" from python script
  		myConsole.log(message);
	});

	pyshell_send.end(function (err) {
  	if (err) throw err;
  		myConsole.log('Finish send');
	});


}

//Streaming functions

function start_stream(){
	var nodeConsole = require('console');
  	var myConsole = new nodeConsole.Console(process.stdout, process.stderr);

	stream = exec('gst-launch-1.0 udpsrc port=5000 ! application/x-rtp,encoding-name=JPEG,payload=26 ! rtpjpegdepay ! jpegdec ! autovideosink', function(error, stdout, stderr) {
    //myConsole.log('stdout: ' + stdout);
    //myConsole.log('stderr: ' + stderr);
    if (error !== null) {
        myConsole.log('Error stream: ' + error);
    }

	});
}

function stop_stream(){
	stream.exit(1);
}