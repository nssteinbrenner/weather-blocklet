# weather-blocklet
Weather blocket for i3-blocks, pulls from DarkSky

The code reads your api key and coordinates from a config file. The format of the config file is below. Note the space between they key/coords and the ':' character, as that is important for the script to properly parse the config file and find the arguments.

api: {apikey}                                                                              
loc: {lat,lon}
