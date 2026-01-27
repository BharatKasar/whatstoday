const express = require("express");

const commonService = require("./services/commonService");

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/api/today", (req, res) => {
    const result = commonService.canDoFromDate();
    res.send(`
        <html>
        <body style="
            display:flex;
            justify-content:center;
            align-items:center;
            height:100vh;
            font-family:sans-serif;
            background:#111;
        ">
            <h1 style="font-size:8rem;color:${result ? "lime" : "red"}">
            ${result ? "YES" : "NO"}
            </h1>
        </body>
        </html>
    `);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
