var path = require('path');
var create  = 0;
var params = "";
var PythonShell = require('python-shell');
var options = {
  pythonOptions: ['-u'],
  scriptPath: __dirname+'/../scripts/reader/'
};

var net = require('net');
var client;

var nodeConsole = require('console');
var myConsole = new nodeConsole.Console(process.stdout, process.stderr);

var exec = require('child_process').exec;
var stream;

var key_list = {"W":"go","A":"left","S":"back","D":"right","Q":"scoop", "O":"cam_l", "P":"cam_r"};
var key_unpressed = {"W":"_go","A":"_left","S":"_back","D":"_right","Q":"_scoop", "O":"_cam_l", "P":"_cam_r"};
var key_pressed_ant = "";

//DOM functions

document.addEventListener('DOMContentLoaded', function() {
  var url = window.location.search.substr(1);
  params = url.split("=")
  document.getElementById("machine_title").innerHTML = params[0] + params[1];
  var client = net.connect(1234,params[2]);
})

document.onkeydown = function(evt) {
    evt = evt || window.event;
    var charCode = evt.keyCode || evt.which;
    var key_pressed = String.fromCharCode(charCode);
    if(key_list[key_pressed] != undefined){
    	if(key_pressed != key_pressed_ant){
    		send_key_pressed(key_list[key_pressed]);
    		key_pressed_ant = key_pressed;
    	}
   	}
}

document.onkeyup = function(evt) {
    evt = evt || window.event;
    var charCode = evt.keyCode || evt.which;
    var key_pressed = String.fromCharCode(charCode);
   	send_key_pressed(key_unpressed[key_pressed_ant]);
   	key_pressed_ant = "";
}

//Fill data functions

function get_data(){
	var pyshell_data = new PythonShell("reader_robot.py",options);
	//Recogida de los mensajes de el script
	pyshell_data.on('message', function (message) {
		myConsole.log("Mensaje de python= " + message);
		if(create == 0) create_panels(message);
		else update_panels(message);
	});

	//Termina el proceso python
	pyshell_data.end(function (err) {
		if (err){
	    	throw err;
		};
		
		myConsole.log('finished');
  	});
}

function create_panels(message_received){
	delete_alert();
	message_received = JSON.parse(message_received.replace(/'/g, '"'));
	myConsole.log(message_received);
	for (var key in message_received){
			document.getElementById("sensors_panel").innerHTML += '<div class="panel panel-default"><div class="panel-heading">'+key+'</div><div class="panel-body" id="'+key+'"></div></div><hr>';
    }
    create = 1;
}

function update_panels(message_received){
	message_received = JSON.parse(message_received.replace(/'/g, '"'));
	for (var key in message_received){
			document.getElementById(key).innerHTML = message_received[key];
    }
}

function delete_alert(){
	var element = document.getElementById("data_alert");
	element.outerHTML = "";
	delete element;
}

//Send data functions
function send_key_pressed(key_pressed){
	myConsole.log("ENVIO");
	client.write(key_pressed);
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
