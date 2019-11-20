const { app, BrowserWindow } = require('electron')

function createWindow () {
  let win = new BrowserWindow({
    width: 500,
    resizable: false,
    height: 300,
    webPreferences: {
      nodeIntegration: true
    }
  })
  win.loadFile('template/index.html')
  win.on('close', (e) => {
    win.loadFile('template/goodbye.html');
    e.preventDefault();
  })
}
app.on('ready', createWindow)