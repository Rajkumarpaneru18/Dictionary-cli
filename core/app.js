require('dotenv').config()

const express = require('express');
const bodyParser = require("body-parser")

const app = express();

app.use(bodyParser.json());

app.use("/dictionary", require("./src/routes/dictionary"))
app.use("/oed", require("./src/routes/oed"))
app.use("/merriam", require("./src/routes/merriam"))

app.use("/google", require("./src/routes/google"))

app.listen(process.env.PORT || 8000);