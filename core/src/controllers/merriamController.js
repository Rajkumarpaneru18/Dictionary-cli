require('dotenv').config();
const { baseController } = require("./baseController");

const merriamView = async (req, res) => {
    await baseController(req, res, process.env.MERRIAM_URL, process.env.MERRIAM_SELECTOR, "www.merriam-webster.com");
};

module.exports = { merriamView }