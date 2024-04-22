const express = require("express")
const { dictionaryView } = require('../controllers/dictionaryController')
const router = express.Router();

router.get('/', dictionaryView);

module.exports = router;