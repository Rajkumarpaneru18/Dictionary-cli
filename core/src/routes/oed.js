const express = require("express")
const { oedView } = require("../controllers/oedController")

const router = express.Router();

router.get('/', oedView);

module.exports = router;