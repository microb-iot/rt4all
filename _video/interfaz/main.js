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

	machine_selector_window.on('closed', () => {
  		app.quit()
	})
});

ipcMain.on( "new_machine_window", ( e, arg ) => {
    //console.log(arg);
    var machine_window = new BrowserWindow({
		height: 700,
		width: 1200,
		resizable: false
	});
    //machine_window.webContents.send('data-id', arg);
	machine_window.loadURL('file://' + __dirname + '/template/machine_window.html?id='+arg);
	
} );