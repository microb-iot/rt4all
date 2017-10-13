var path = require('path');

var PythonShell = require('python-shell');
var options = {
  pythonOptions: ['-u'],
  scriptPath: __dirname+'/../scripts/reader/'
};

var nodeConsole = require('console');
var myConsole = new nodeConsole.Console(process.stdout, process.stderr);

var machines_list = new Array();

function add_option(id,message){
  myConsole.log("Lista actual: " + machines_list);;
    var selector = document.getElementById(id);
    var option = document.createElement("option");
    option.text = message["machine"].toString() +" - " +  message["machine_id"].toString();
    myConsole.log(message["machine"].toString());
    val = message["machine_id"].toString() + ";" + message["machine_ip"].toString();
    myConsole.log(val);
    option.value = val;
    selector.add(option);
}

function load_machines(){
  var pyshell = new PythonShell("sub_machines.py",options);
  //Recogida de los mensajes de el script
  pyshell.on('message', function (message) {
    message_received = JSON.parse(message.replace(/'/g, '"'));
    if(machines_list.indexOf(message_received["machine_ip"].toString()) == -1){
      machines_list.push(message_received["machine_ip"].toString());
      add_option("selector",message_received);
    }
  });

  //Termina el proceso python
  pyshell.end(function (err) {
    if (err){
        throw err;
  };
    document.getElementById("loader").style.display = "none";
    document.getElementById("form_selector").style.display = "block";
    document.getElementById("recharge_icon").style.display = "none";
    myConsole.log('finished');
  });

}

function recharge(){
  document.getElementById('selector').options.length = 0;
  machines_list = new Array();

  document.getElementById("recharge_icon").style.display = "inherit";
  load_machines();
}

