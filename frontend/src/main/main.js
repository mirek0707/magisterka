import path from 'path'

const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 1024,
    height: 640,
    minWidth: 600,
    minHeight: 400,
    autoHideMenuBar: true
  })


  win.loadFile(path.join(__dirname, "../renderer/index.html"))
  win.webContents.openDevTools()
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
