# <p align="center">Dictionary CLI</p>
<p align="center">
    <a href="https://github.com/Rajkumarpaneru18/Dictionary-cli/watchers" target="_blank">
        <img src="https://img.shields.io/github/watchers/Rajkumarpaneru18/Dictionary-cli?style=for-the-badge&logo=appveyor" alt="Watchers"/>
    </a>
    <a href="https://github.com/Rajkumarpaneru18/Dictionary-cli/network/members" target="_blank">
        <img src="https://img.shields.io/github/forks/Rajkumarpaneru18/Dictionary-cli?style=for-the-badge&logo=appveyor" alt="Forks"/>
    </a>
    <a href="https://github.com/Rajkumarpaneru18/Dictionary-cli/stargazers" target="_blank">
        <img src="https://img.shields.io/github/stars/Rajkumarpaneru18/Dictionary-cli?style=for-the-badge&logo=appveyor" alt="Star"/>
    </a>
</p>
<p align="center">
    <a href="https://github.com/Rajkumarpaneru18/Dictionary-cli/issues" target="_blank">
        <img src="https://img.shields.io/github/issues/Rajkumarpaneru18/Dictionary-cli.svg?style=for-the-badge&logo=appveyor" alt="Issue"/>
    </a>
    <a href="https://github.com/Rajkumarpaneru18/Dictionary-cli/pulls" target="_blank">
        <img src="https://img.shields.io/github/issues-pr/Rajkumarpaneru18/Dictionary-cli.svg?style=for-the-badge&logo=appveyor" alt="Open Pull Request"/>
    </a>
</p>
<p align="center">
    <a href="https://github.com/Rajkumarpaneru18/Dictionary-cli/blob/main/LICENSE" target="_blank">
        <img src="https://img.shields.io/github/license/Rajkumarpaneru18/Dictionary-cli?style=for-the-badge&logo=appveyor" alt="License" />
    </a>
</p>
<p align="center">
  <a href="https://github.com/Rajkumarpaneru18/Dictionary-cli" style="font-size: 24px;">Dictionary CLI</a>
  <span style="font-size: 20px;">A command-line interface (CLI) tool designed to quickly find the meaning of words without the need for a web browser.</span><br>
  <span style="font-size: 16px;">Stay focused during study or exam time by accessing word meanings directly in your terminal!</span><br>
</p>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usages](#usages)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Problem Statement
In academic environments or situations where distractions need to be minimized, accessing online dictionaries or search engines to find word meanings can be counterproductive. Dictionary CLI solves this problem by providing a fast and distraction-free way to look up word meanings directly within the terminal.

## Features 
- Instant Word Definitions: Quickly find the meanings of words without leaving the terminal.
- Efficiency: Avoid distractions and save time during study or exam periods.
- Accessibility: Access word meanings even in environments with restricted internet access.


## Demo

https://github.com/SusheelThapa/from_taipy_census/assets/83917129/95d90f86-e1e4-4883-ae15-a3f4af116e7f

## Installation
1. Clone the repository 
   ```
   git clone https://github.com/Rajkumarpaneru18/Dictionary-cli.git

   ```

### Backend
1. Change the directory to core
    ```
    cd core

   ```
2. Installation of Node.js packages
   ```
   npm install
   
   ```
3. Install the Puppeteer 
   ```
    npm install puppeteer
   
   ```

iv. add .env file to 
```
BROWSERLESS_URL=ws://localhost:3000?token=6R0W53R135510
PORT=5000
DICTIONARY_URL=http://www.dictionary.com/browse/
DICTIONARY_SELECTOR=ol > li:nth-child(1) >span> .NZKOFkdkcvYgD3lqOIJw
OED_URL=http://www.oed.com/search/dictionary/?scope=Entries&q=
OED_SELECTOR=.snippet
MERRIAM_URL=http://www.merriam-webster.com/dictionary/
MERRIAM_SELECTOR=div > span > .dtText
GOOGLE_URL=https://www.google.com/search?q=
```
### CLI
1. change the directory to cli
   ```
   cd cli
  
   ```
2. install
   ```
   npm install nodemon --save-dev
   
    ```
### To run program
1. run the docer
   ```
   #! /bin/bash

   sudo docker run --rm -p 3000:3000 -e MAX_CONCURRENT_SESSIONS=10 browserless/chrome:latest
   ```
2. run backend
    ```
    npm run dev
   ```
3. run cli
    ```
    ./cli.py -i
     ./cli.py -g (word to search from google)
    ./cli.py -m (word to search from merriam-webster)

   ```
## Usages
- Quick Word Definitions: Simply enter the word you want to look up, and Dictionary CLI will fetch and display its meaning from online sources.
- Distraction-Free: Stay focused on your tasks without the need to open a web browser or navigate through online dictionaries.
- Customizable: Add or modify sources to tailor the word meanings to your preferences or requirements.

## Dependencies
- Node.js
- Puppeteer

## Contributing
Contributions to enhance and improve Dictionary CLI are welcome! Feel free to submit issues, feature requests, or pull requests. Please adhere to our Code of Conduct.


## License

This project is licensed under the [MIT License](/LICENSE).
