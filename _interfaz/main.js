const {app, BrowserWindow, ipcMain, dialog} = require('electron');
//const ipc = require('electron').ipcMain;

app.on('window-all-closed', () => {
  app.quit()
})

app.on('ready', () => {

	var machine_selector_window = new BrowserWindow({
		height: 500,
		width: 300,
		resizable: false,
	});
	machine_selector_window.loadURL('file://' + __dirname + '/template/machine_selector.html');
	machine_selector_window.setPosition(20, 80);
	machine_selector_window.on('closed', () => {
  		app.quit()
	})
});

ipcMain.on( "new_machine_window", ( e, arg ) => {
    //console.log(arg);
    var machine_window = new BrowserWindow({
		height: 800,
		width: 800,
		resizable: false
	});
    //machine_window.webContents.send('data-id', arg);
	machine_window.loadURL('file://' + __dirname + '/template/machine_window.html?'+arg);
	machine_window.webContents.openDevTools();
	machine_window.setPosition(400,5);
} );