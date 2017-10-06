var path = require('path');
var PythonShell = require('python-shell');
var script = "test.py"

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
  var pyshell = new PythonShell(script);

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
    myConsole.log('finished');
  });

}

