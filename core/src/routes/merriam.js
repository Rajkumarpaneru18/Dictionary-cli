const express = require("express")
const { merriamView } = require("../controllers/merriamController");

const router = express.Router();

router.get('/', merriamView);

module.exports = router;