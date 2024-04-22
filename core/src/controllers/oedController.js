require('dotenv').config()

const { baseController } = require("./baseController");

const oedView = async (req, res) => {
    await baseController(req, res, process.env.OED_URL, process.env.OED_SELECTOR, "www.oed.com");
};

module.exports = { oedView }