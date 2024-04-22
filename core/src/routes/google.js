const express = require("express");
const { googleView } = require("../controllers/googleController");
const router = express.Router();

router.get('/', googleView);

module.exports = router;