# dynstatus
Dynstatus tries to pinpoint your location based on your network configuration (WLAN, IP, ...) and enables you to run code to react to changes.

## Operation Modes
You can use dynstatus in three different ways

### Just execute it
Dynstatus will detect your location and run your plugins once.  
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
