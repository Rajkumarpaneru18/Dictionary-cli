require('dotenv').config()

const { baseController } = require("./baseController")

const dictionaryView = async (req, res) => {
    await baseController(req, res, process.env.DICTIONARY_URL, process.env.DICTIONARY_SELECTOR, "www.dictionary.com");
};

module.exports = { dictionaryView }