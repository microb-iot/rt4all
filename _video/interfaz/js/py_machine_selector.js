var path = require('path');

var PythonShell = require('python-shell');
var options = {
  pythonOptions: ['-u'],
  scriptPath: __dirname+'/../scripts'
};

var machines_list = new Array();

function add_options(id,lista){
  var selector = document.getElementById(id);
  for (i = 0; i < lista.length; i++) {
    var option = document.createElement("option");
    option.text = lista[i].toString();
    selector.add(option);
  }  
}

function load_machines(){
  var nodeConsole = require('console');
  var myConsole = new nodeConsole.Console(process.stdout, process.stderr);
  var pyshell = new PythonShell("test.py",options);

  //Recogida de los mensajes de el script
  pyshell.on('message', function (message) {
    myConsole.log(message);
    machines_list.push(message.toString());
  });

  //Termina el proceso python
  pyshell.end(function (err) {
    if (err){
        throw err;
    };
    add_options("selector",machines_list);
    document.getElementById("loader").style.display = "none";
    document.getElementById("form_selector").style.display = "block";
    myConsole.log('finished');
  });

}

