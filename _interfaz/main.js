const {app, BrowserWindow, ipcMain, dialog} = require('electron');
var path = require('path')
//const ipc = require('electron').ipcMain;
app.commandLine.appendSwitch('ignore-certificate-errors');

app.on('window-all-closed', () => {
  app.quit()
})

app.on('ready', () => {

	var machine_selector_window = new BrowserWindow({
		height: 500,
		width: 300,
		resizable: false,
		icon: path.join(__dirname, '/template/assets/icon/program_icon.png')
	});
	machine_selector_window.loadURL('file://' + __dirname + '/template/machine_selector.html');
	machine_selector_window.setPosition(20, 80);
	//machine_selector_window.webContents.openDevTools();
	machine_selector_window.on('closed', () => {
  		app.quit()
	})
});

ipcMain.on( "new_robot_window", ( e, arg ) => {
    //console.log(arg);
    var machine_window = new BrowserWindow({
		height: 700,
		width: 800,
		resizable: false
	});
    //machine_window.webContents.send('data-id', arg);
	machine_window.loadURL('file://' + __dirname + '/template/machine_window.html?'+arg);
	//machine_window.webContents.openDevTools();
	machine_window.setPosition(400,5);
} );

ipcMain.on( "new_Shovel_window", ( e, arg ) => {
    //console.log(arg);
    var machine_window = new BrowserWindow({
		height: 500,
		width: 500,
		resizable: false
	});
    //machine_window.webContents.send('data-id', arg);
	machine_window.loadURL('file://' + __dirname + '/template/shovel_window.html?'+arg);
	//machine_window.webContents.openDevTools();
	machine_window.setPosition(400,5);
} );
