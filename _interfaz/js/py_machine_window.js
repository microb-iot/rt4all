//JS code for the machine window

// Setup variables and packets

var path = require('path');
var net = require('net');
var create  = 0;
var params = "";
var PythonShell = require('python-shell');
var options = {
  pythonOptions: ['-u'],
  scriptPath: __dirname+'/../scripts/reader/'
};

// Create a variable for the socket connection
var client;
var nodeConsole = require('console');
var myConsole = new nodeConsole.Console(process.stdout, process.stderr);

var exec = require('child_process').exec;
var stream;

// Dictionary for the pressed keys and their unpressed code
var key_list = {"W":"go","A":"left","S":"back","D":"right","Q":"scoop", "O":"cam_l", "P":"cam_r","9":"Goodbye"};
var key_unpressed = {"W":"_go","A":"_left","S":"_back","D":"_right","Q":"_scoop", "O":"_cam_l", "P":"_cam_r","9":"_Goodbye"};
var key_pressed_ant = "";

// DOM functions
document.addEventListener('DOMContentLoaded', function() {
  var url = window.location.search.substr(1);
  params = url.split("=")
  // Receive the data needed with `get` params:
  // id, name and ip
  document.getElementById("machine_title").innerHTML = params[0] +"#"+ params[1];
  // Start the socket connection in the specific port to the ip selected
  client = net.connect(1234,params[2]);
})

// Read from the page if a key is pressed, only once, and then send it
document.onkeydown = function(evt) {
    evt = evt || window.event;
    var charCode = evt.keyCode || evt.which;
    var key_pressed = String.fromCharCode(charCode);
    //Check if the key pressed is in the list
    if(key_list[key_pressed] != undefined){
    	// If the key was not pressed before, it send
    	if(key_pressed != key_pressed_ant){
        toggle_bold_key_panel(key_list[key_pressed]);
    		send_key_pressed(key_list[key_pressed]);
    		key_pressed_ant = key_pressed;
    	}
   	}
}

// Read from the page if the key was unpreesed, and send the correct value
document.onkeyup = function(evt) {
    evt = evt || window.event;
    var charCode = evt.keyCode || evt.which;
    var key_pressed = String.fromCharCode(charCode);
    if(key_unpressed[key_pressed] != undefined){
      toggle_bold_key_panel(key_list[key_pressed]);
   	  send_key_pressed(key_unpressed[key_pressed_ant]);
      key_pressed_ant = "";
    }
}

//Fill data functions

// Function that start when the page loads and reads data from RTI script
function get_data(){
	var pyshell_data = new PythonShell("reader_robot.py",options);
	// Start the pyshell data and receive the messages from it
	pyshell_data.on('message', function (message) {
		myConsole.log("Mensaje de python= " + message);
    document.getElementById("controls_panel").style.display="block";
    document.getElementById("report_button").style.display="inline";
		// Create the panels for the DOM, and if created, update 
		if(create == 0) create_panels(message);
		else update_panels(message);
	});

	// Pyshell ends
	pyshell_data.end(function (err) {
		if (err){
	    	throw err;
		};
		
		myConsole.log('finished');
  	});
}

// Create the panels with the data received, it generates it with only one packet of data
function create_panels(message_received){
	delete_alert();
	message_received = JSON.parse(message_received.replace(/'/g, '"'));
	myConsole.log(message_received);
  if(message_received["cam"] == 1) document.getElementById("streaming_button").style.display="inline";
	for (var key in message_received){
    if(key !="cam") document.getElementById("sensors_panel").innerHTML += '<div class="panel panel-default"><div class="panel-heading" style="background-color: #d0d0d0;">'+key+'</div><div class="panel-body" id="'+key+'"></div></div>';
  }
  create = 1;
}

// Update the panels when created, controlled used the variable `created`
function update_panels(message_received){
	message_received = JSON.parse(message_received.replace(/'/g, '"'));
	for (var key in message_received){
    if(key !="cam") document.getElementById(key).innerHTML = message_received[key];
    }
}

// Delete the alert dialog when the window is not receiving data.
function delete_alert(){
	var element = document.getElementById("data_alert");
	element.outerHTML = "";
	delete element;
}

// Send the `key_pressed` to the socket
function send_key_pressed(key_pressed){
	myConsole.log("ENVIO");
	client.write(key_pressed);
}

//Streaming functions

// Call the exec function to start the stream with the gstreamer library
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

function reconnect_button(){
    client = net.connect(1234,params[2]);
}


function toggle_sshterminal(){
    var x = document.getElementById("ssh_terminal");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function toggle_bold_key_panel(id){
  acc_style = document.getElementById(id);
  if(acc_style.className == "font_regular") acc_style.className = "font_bold";
  else acc_style.className = "font_regular";
}

function generate_report(){
  var options_report = {
    pythonOptions: ['-u'],
    scriptPath: __dirname+'/../report/',
    args: ['Pedro','Crane','0','192.168.1.137']
  };
  var pyshell_report = new PythonShell("logger.py",options_report);
  pyshell_report.on('message', function (message) {
    myConsole.log(message);
  });

  pyshell_report.end(function (err) {
    if (err){
        throw err;
    };
    myConsole.log('finished');
  });
}