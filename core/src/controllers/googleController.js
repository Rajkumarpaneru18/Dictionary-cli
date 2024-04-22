require('dotenv').config()

const puppeteer = require('puppeteer-core')

const googleView = async (req, res) => {

    const searchWord = req.body['search-word']

    const browser = await puppeteer.connect({
        browserWSEndpoint: process.env.BROWSERLESS_URL
    })

    const page = await browser.newPage();

    await page.setViewport({ width: 1920, height: 1024 });

    await page.goto(process.env.GOOGLE_URL + searchWord, { waitUntil: "domcontentloaded" })

    const data = await page.screenshot();
    browser.close();

    return res.end(data, 'binary')

}

module.exports = { googleView }