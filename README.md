# PSLab Desktop :gemini:

> Electron desktop app for an awesome openhardware platform. Made with love :purple_heart:

<a href="https://pslab.io/" rel="some text">![Foo](https://steemitimages.com/p/99pyU4b7LirZqBVNm82rKVQvTzrDG2Wf2k7FTDVtTcQsQ1UCQPXzwnZtrAgwekLbqiKKsoxRbLwRqb3JaFhi32BRuQFapgf3zN3U4EWxpkCLEK8si2VfvZCEFXXMeudjGS?format=match&mode=fit&width=640)</a>  
This project is a reimplementation of the PSLab Desktop orginally developed using the python stack. As of now, we are working on replicating features of the android app one by one.

# How to contribute
In order to contribute, we would recommend you to first read the [community guidelines](https://blog.fossasia.org/open-source-developer-guide-and-best-practices-at-fossasia/) as stated by FOSSASIA.

## Setup  :metal:
1. Fork the project to get a copy of the repository in your github profile.
2. Clone the copied project from your profile ( Not the original repository from FOSSASIA ).
3. ```cd``` into your project folder.
4. ```git remote add upstream https://github.com/fossasia/pslab-desktop.git``` This command will set up the upsteam link.

## Installation :snowflake:
While in your project folder
```bash
npm install
```
This command will install all the necessary dependencies required by the electron app to run.  
  
As this app uses the **PSL** library under the hood for device communication, you'll have to install it as well.
The instructions to install it are provided [here](https://github.com/fossasia/pslab-python).
After installation of **PSL** make sure you can property import it in **Python3**. Run the following command in your bash shell.
```bash
python3
>>> from PSL import sciencelab
```
If this command runs without throwing an error, then we are good to go.

## Starting the app :zap:
Everything command to start and debug the app are writen in package.json. To simply get it running run the following command while in your project repository.
```bash
npm start
```
And wait for the electron shell to open. 
Happy coding!  :fire: