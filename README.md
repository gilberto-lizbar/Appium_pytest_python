# Appium_pytest_python

Python, Selenium Installation Guide Download
Installing Python and Selenium

Installing Python:

Windows : http://python.org/download/.

Note : IF you are using Linux, MacOS X, Unix operating Systems then python will be installed by default with OS

**1.What is PIP installer Tool?**

pip is a package management system used to install and manage software packages written in Python

pip is a recursive acronym that can stand for either "Pip Installs Packages" or "Pip Installs Python

**2.Where do we get this PIP Tool?** 

Included with Python Installations: In most cases, when you install Python (versions 2.7.9+ or 3.4+), 
pip is automatically included and installed alongside it. This is the most common and recommended method for acquiring pip.

Separate Installation on Some Linux Systems: On certain Linux distributions like Ubuntu, pip might be packaged separately as python3-pip.
In such cases, you would install it using your system's package manager, for example:

sudo apt install python3-pip

**3.Installing Selenium**

Use Below command on PIP to install Selenium Package

**pip install selenium**

This command will set up the Selenium WebDriver client library on your machine with all modules and classes that we will need to create automated scripts using Python

**4. Upgrade selenium**

**pip install -U selenium**

The optional –U flag will upgrade the existing version of the installed package

**5. Python Library to read/write excel files**

**pip install openpyxl**

# Pytest

**6. Install Pytest and Configuration**

**pip install pytest**

**Configure/Run Pytest in PyCharm**
- Select Edit Configurations (Run>Edit Configurations…)
- Select Add New Configuration ('+' button)
- Select pytest option from Python tests
- Clicks on Apply and OK button
- Once pytest run configuration appears on navigation bar, 
clicks on dropdown and select Edit Configuration 
- From Target options checks Scripts path and selects the path for your test
- Select Apply and OK 
- Once pytest configuration appears in Navigation bar click on Run button to execute the test
**Run Pytest in Terminal**
  - From terminal navigate to the path where pytest are located example: 
  cd /Users/gilberto.barraza/Desktop/Repo_Cursos/Selenium_WebDriver_Python/PytestDemo

**7. Pytest execution commands**
  
  **py.test** # execute all pytest from path folder
  
  **py.test [test_name.py]** # execute file given file (example: py.test test_demo1.py)
  
  **py.test -v** # -v print executed methods on tests from path folder
  
  **py.test -v -s** # -s print console logs

  **py.test -k [text]** # -k [text] find and run test methods from actual folder which contains the given text
  (example: py.test -k CreditCard)

  **Using tags**

  **py.test -m [tag]** # -m [mark] This will run all the tests which contains the mark/tag from actual folder
  - (example: py.test -m smoke) executes the tests with 'smoke' mark which belongs to method test_secondGreetCreditCard
  
  @pytest.mark.smoke 
  
  def test_secondGreetCreditCard():
  
  - If a method contains skip mark, test won't be executed and will be reported as skipped on results
  
  @pytest.mark.smoke

  @pytest.mark.skip
  
  def test_firstProgram():
  
  - If a method contain xfail mark, It means a test will be executed but not reported as fail it will 
  be reported as XPASS instead, You can add xfail tag when need to run a test even you know it fails or 
  has a dependency where need to run a particular test for further tests
  
  @pytest.mark.smoke

  @pytest.mark.xfail
  
  def test_firstProgram():

# Assertions

**8. Using pytest-check**
  The pytest-check plugin is widely recommended for soft assertions. 
  1. Installation:

    pip install pytest-check
    
    OR
    
    Navigate to Settings > Project:[name] > Python Interpreter > + > Search ‘pytest-soft-assertions’ > Install Package
 

# Reports

**9. Install Pytest html reports**

    pip install pytest-html

 # Parallel Mode pytest-xdist Installation

  pip install pytest-xdist

  
# Parallel Mode pytest- Execution commands

  pytest -n 10  # To specify a specific number of parallel processes (e.g., 4 processes)

  py.test -n 2 tests -m smoke -v -s --browser_name Chrome

  py.test -n 2 tests/test_frameExample.py --html reports/report.html -v -s # execute pytest from path generating reports


