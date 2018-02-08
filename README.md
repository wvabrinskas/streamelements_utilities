# streamelements_utilities 
- Utilities for controlling StreamElements with the Elgato StreamDeck Edit Add topics


# Pre-Setup Instructions
1. *Windows Users Only*: Please install Python from [here](https://www.python.org/downloads/windows/)
1. Open up `config-example.json` in a text editor and add the required fields:
    - Replace where it says `JWT-TOKEN-GOES-HERE` with your token from your StreamElements account.
    - Replace where it says `CHANNEL-ID-GOES-HERE` with your channel ID from your StreamElements account.
    - These can be found on the by clicking on your user name in the top left and going to `Settings` and then clicking `Accounts`. Or by clicking [here](https://streamelements.com/dashboard/account/information) to take you right to it. 
1. Rename `config-example.json` to `config.json`

# Song Requests
## Install Instructions for Stream Deck
1. Open up `Stream Deck` software and add two `Open` actions to the board. 
1. Label one action `Start` and the other action `Stop`.
1. Link the `start.py` file to the `Start` action. Link the `stop.py` file to the `Stop` action. 
    - *Windows Users*: Link `start.bat` to `Start` and `stop.bat` to `Stop`

# Developer Social Contact
1. [Twitter](https://twitter.com/william_vab)
1. [Twitch (wavOW)](https://twitch.tv/wavow)
1. [Twitch (Gaming Night Live)](https://twitch.tv/gamingnightlive)