const express = require("express");

const commonService = require("./services/commonService");

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/api/today", (req, res) => {
    const result = commonService.canDoFromDate();
    res.send(result);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
