//JS code for the machine selector window

// Setup variables and packets
var path = require('path');

var PythonShell = require('python-shell');
var options = {
  pythonOptions: ['-u'],
  scriptPath: __dirname+'/../scripts/reader/'
};

var nodeConsole = require('console');
var myConsole = new nodeConsole.Console(process.stdout, process.stderr);

var machines_list = new Array();

//
// Function that adds an option to the dropdown
//
// `id` - The id of the dropdown
//
// `machine_data` - Data of the machine to add
//
function add_option(id,machine_data){
  myConsole.log("Lista actual: " + machines_list);;
  var selector = document.getElementById(id);
  var option = document.createElement("option");
  option.text = machine_data["machine"].toString() +" - " +  machine_data["machine_id"].toString();
  val = machine_data["machine"].toString() + "=" + machine_data["machine_id"].toString() + "=" + message["machine_ip"].toString();
  myConsole.log(val);
  option.value = val;
  selector.add(option);
}

//
// Start function that connects to rti and get 
// the id, ip and name of the machine connected in the local network.
//
function load_machines(){
  var pyshell = new PythonShell("sub_machines.py",options);
  // Pyshell `on` starts a python shell with the
  // script indicated and waits for receive a message
  pyshell.on('message', function (message) {
    message_received = JSON.parse(message.replace(/'/g, '"'));
    // Check if the machine is added, if not it creates an option in the dropdown
    if(machines_list.indexOf(message_received["machine_ip"].toString()) == -1){
      machines_list.push(message_received["machine_ip"].toString());
      add_option("selector",message_received);
    }
  });
  // PyShell ends
  pyshell.end(function (err) {
    if (err){
        throw err;
    };
    // When the pyshell ends it close the loading spinner and shows the dropdown
    document.getElementById("loader").style.display = "none";
    document.getElementById("form_selector").style.display = "block";
    document.getElementById("recharge_icon").style.display = "none";
    myConsole.log('finished');
  });
}


// Updates the dropdown

function recharge(){
  document.getElementById('selector').options.length = 0;
  machines_list = new Array();

  document.getElementById("recharge_icon").style.display = "inherit";
  load_machines();
}

