# RaspberryPi_ThermoFan
Python Script and Circuit to allow for your Raspberry Pi Fan to be triggered when the CPU reaches a set temperature

## Installation Instructions

1. Copy *thermo_fan.py* into */etc/init.d/*
1. Edit settings in file, if needed
1. Set Permissions to allow file to be Executed - `sudo chmod +x thermo_fan.py`
1. Set to Run Script on Boot - `sudo update-rc.d thermo_fan.py defaults`
1. Done!

### Express Installation

1. Login to Device via SSH
1. Run `sudo curl https://raw.githubusercontent.com/lucanos/RaspberryPi_ThermoFan/master/thermo_fan.py --output thermo_fan.py;sudo chmod +x thermo_fan.py;sudo update-rc.d thermo_fan.py defaults`

## Settings
### Pin
The GPIO Pin which is connected to the Base pin on the Transistor. Default: 18
### Check Interval
The number of seconds to wait between checks of the CPU Temperature. Default: 5
### Temp Trigger (Fan On Temperature)
The temperature (in Celsius) at which the fan with switch on. Default: 60
### Temp Detrigger (Fan Off Temperature)
The temperature (in Celsius) at which the dan will switch off. Default: 55
