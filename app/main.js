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
  win.loadFile('index.html')
}
app.on('ready', createWindow)