require('dotenv').config()

const puppeteer = require("puppeteer-core")

const baseController = async (req, res, websiteURL, meaningSelector,source) => {
    const searchWord = req.body['search-word'];

    const browser = await puppeteer.connect({
        browserWSEndpoint: process.env.BROWSERLESS_URL
    })

    const page = await browser.newPage();

    await page.setViewport({ width: 1920, height: 1024 });

    await page.goto(websiteURL + searchWord, { waitUntil: "domcontentloaded" })


    const searchWordMeaning = await page.evaluate((meaningSelector) => {
        return document.querySelector(meaningSelector)?.innerText || "Meaning not found"
    }, meaningSelector);

    const response = { 'word': searchWord, "meaning": searchWordMeaning, 'source': source }

    browser.close();

    res.send(response);
    res.end();

}

module.exports = {baseController}