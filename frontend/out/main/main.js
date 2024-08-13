"use strict";
const { app, BrowserWindow } = require("electron");
const createWindow = () => {
  const win = new BrowserWindow({
    width: 1024,
    height: 640,
    minWidth: 600,
    minHeight: 400,
    autoHideMenuBar: true
  });
  win.loadURL("http://localhost:5173");
};
app.whenReady().then(() => {
  createWindow();
  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
