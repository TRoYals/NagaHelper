require("chromedriver");
const { Builder } = require("selenium-webdriver");
options.addArguments(
  "--user-data-dir=/Users/fuqixuan/Library/Application Support/Google/Chrome/Default"
);
driver = new Builder().forBrowser("chrome").build();
