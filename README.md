# ToDoMVC React Automated Checks using Python and SeleniumBase

## Running SeleniumBase UI Tests

### Dependencies

* [SeleniumBase](https://seleniumbase.io/)
* SeleniumBase driver for your desired browser. Run `seleniumbase install chromedriver` for *Google Chrome* or `seleniumbase install geckodriver` for *Firefox*.

---

### Headlessly

1. Open a web browser. Go to the remote code repository (<https://github.com/jasonogayon/autochecks-py-seleniumbase>) and copy its SSH or HTTPS link.

2. On your machine, open a terminal and clone the remote repository locally wherever you want. Run `git clone git@github.com:jasonogayon/autochecks-py-seleniumbase.git`.

3. After that, go inside the cloned **autochecks-py-seleniumbase** repository. You can decide to rename this directory to what you want.

4. Now we can run our tests locally on our machine. Run `make h`.

---

### With Browser Launching

1. Follow the same steps 1-3 above.

2. Run `make ui`

---

### On Demo Mode

SeleniumBase has a neat *demo mode* feature. The tests will highlight the elements that are targetted for every step. To run the tests on this mode:

1. Follow the same steps 1-3 above.

2. Run `make demo`

---

![Sample SeleniumBase Test Report](./docs/12242021-test-report.png)

### Reports

Running the tests on whatever mode generates a test report in HTML format, found inside the **report** directory. If there any one test fails, a screenshot of where the failure occured is automatically included in the report.

Author: Jason B. Ogayon \
Software Engineer and Software Tester