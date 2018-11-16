# pySearch

pySearch is a simple command line python script that allows for seamlessly performing a web search without removing your hands off the keyboard as it opens a new browser tab to search the input string. Normally when working on a command line interface, a user would need to use their mouse to perform a web search as they would take one hand off the keyboard and navigate to their browser. Even when using ALT+TAB, users would still need to navigate to the search bar with the mouse and then return to the keyboard to type their search. 

pySearch simplifies this to a single command line command.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python  3 - https://www.python.org/downloads/ 

### Installing

Clone this Repo  

In either Command Prompt for Windows or Terminal for OSX and Linux run: `python <pySearch directory>\pySearch.py -s <search query>`

#### Command Line Arguments 
- `-s`  takes query to search
  * multiple searches can be performed with multiple `-s` delimiters
  * use quotes(" ") if searches contain `-s`
- `-e`  changes name or alias of search engine and sets it to as search engine for session 
- `-d`  changes to domain extension 
- `-h`  provides a description of each command line argument


## Running the tests

pySearch tests use the [pytest](https://docs.pytest.org) library which is not part of the default Python library. If this is the first time pytest tests are being run on the machine use `pip install -r requirements.txt` to install pytest and it's dependencies (NOTE your `pip` alias may differ based on your installation). Afterwards pySearch tests can be run with the `pytest` command when inside the pySearch directory.

## Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

( To Be added )


## Authors

* **Alex Kong** - *Initial work* ( https://github.com/jrkong )

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. (TO be added) 


## Objective 

The goal of pySearch is to bring web search capabilities to your command line so initiating a web search doesn't require taking your hand off the keyboard. The current goal is to integrate as much of the web search workflow into the command line so users can get all the keyboard interaction out of the way before taking one hand off the keyboard to use the mouse to interact with the browser.

### Specific Goals 

 - Support webcrawling which would allow basic searches 
      * Basic dictionary lookup would be a great test case for this, to be performed before opening a browser (think Unix man pages. 
 - Basic browser interactivity through pySearch 
   * The ability to navigate and control your browser using pySearch (so scrolling, selecting and opening search links, open a new tab)
 - pySearch's interactive mode shouldn't impede the user's ability to use command line commands 
  * While it allows keyboard interactivity with the browser while inside the command line it should have the ability to pipe command line commands to the shell and return their output to the user


