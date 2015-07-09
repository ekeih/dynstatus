# dynstatus
Dynstatus tries to pinpoint your location based on your network configuration (WLAN, IP, ...) and enables you to run code to react to changes.

## Setup
You have to copy ```example_config.py``` to ```$XDG_CONFIG_HOME/dynstatus/config.py```. Usually this will mean ```~/.config/dynstatus/config.py```. Afterwards you should modify the configuration to your needs. Make sure that ```plugins_path``` is configured correctly. The configuration should be self-explaining.

## Operation Modes
You can use dynstatus in three different ways

### Just execute it
Dynstatus will detect your location and run your plugins once. You could use this mode in the hooks of your network management tool to react to changes in your network configuration.
```
user@linux$ dynstatus
```
### Run it as a daemon
Dynstatus will fork to background and detect your location and run your plugins periodically. The interval is configured in the ```config.py``` of dynstatus.
```
user@linux$ dynstatus daemon
```

### Get current status information
Dynstatus can give you status information without running the plugins. You can ask for every location setting of your ```config.py```.
```
user@linux$ dynstatus get ssid
```
