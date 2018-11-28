# <img src='https://rawgithub.com/FortAwesome/Font-Awesome/master/advanced-options/raw-svg/solid/robot.svg' card_color='#485EAA' width='50' height='50' style='vertical-align:bottom'/> Fallback Chatbot
Fallback using any offline AIML2.0 chatbot

## About 
**WARNING**: Do NOT install this skill if you aren't at least somewhat familiar with linux as it WILL break your Picroft installation!!!
Because of the mere size of Program-Y, there are a few incompatibilities and installation difficulties that have to be manually resolved.
Please read the whole description before proceeding.
  
<br/>
This skill makes use of the offline Python AIML2.0 interpreter Program-Y.
<br/><br/><br/>

At the moment, it only supports my own stupid bot called BakaBot, but adding your own bots will be supported very soon.

Some dependencies of Program-Y have to be installed with a pip version prior to 10. If the automatic installation of dependencies doesn't work, try downgrading to pip 9.0.3 first:
`pip install pip==9.0.3`.

Then, install Program-Y manually using `pip install programy`.

This will break Mycroft in its current state as one of the dependencies requires `websocket-client>=0.35.0` to work. As a result, pip will update websocket-client to a version that Mycroft in turn does not support anymore. Downgrade to 0.35.0 and you should be fine:

```pip install websocket-client==0.35.0```

If the lxml install fails, do the following:
```
sudo apt install -y libxml2-dev libxslt1-dev zlib1g-dev python3-pip
sudo pip3 install lxml
```
Note that the installation of lxml can be _very_ slow on low RAM devices like the Raspberry Pi (I am talking in the order of 10min+!). If you
ever doubt that it's even doing anything, open another terminal and run `htop` on it.

## Examples 
* ""My name is Dave.""
* ""What is my name?""

## Credits 
Conny Lin @Fantailed

## Supported Devices 
Picroft

Linux Desktop

## Category
Daily
**Entertainment**

## Tags
\#chatbot
\#aiml
\#aiml2.0
