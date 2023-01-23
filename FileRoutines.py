import configparser
from io import StringIO
import GlobalVars
from GlobalVars import Settings
import inspect

from configparser import ConfigParser

class CaseSensitiveConfigParser(ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

def readconfig():

    default_config = {'Settings': dict(filter(lambda item: not item[0].startswith("__"), vars(Settings).items()))}
   # print(default_config)

    config = CaseSensitiveConfigParser()

    config_file = 'FFBcountersteer.cfg'
    try:
        config.read(config_file)
    except configparser.Error as e:
        GlobalVars.InternalVars.InternalConfigFileError = f'Error reading config file: {e}'

    for section, options in default_config.items():
        if not config.has_section(section):
            config.add_section(section)
        for option, value in options.items():
            if not config.has_option(section, option):
                config.set(section, option, str(value))

    config_string = StringIO()
    config.write(config_string)
    config_str = config_string.getvalue()
    print(config_str)
    options = config.items('Settings')
    for option, value in options:
        #setattr(GlobalVars, 'Settings', type('Settings', (GlobalVars.Settings,), {option: value}))
        exec("GlobalVars.Settings."+str(option)+"="+str(value))

        #GlobalVars.Settings.__dict__[option]=value
        #GlobalVars.Settings.LFSSteerAngle = 77
       # print(GlobalVars.Settings.LFSSteerAngle)

def ConfigWrite():
    #global config
    config_file = 'FFBcountersteer.cfg'
    config = CaseSensitiveConfigParser()
    default_config = {'Settings': {name: getattr(Settings, name) for name in dir(Settings) if not name.startswith('__') and not inspect.ismethod(getattr(Settings, name))}}
    #print(dir(Settings))
   # print("222",default_config)
    for section, options in default_config.items():
        if not config.has_section(section):
            config.add_section(section)
        for option, value in options.items():
            config.set(section, option, str(value))
            #print(option, "   ", str(value))

    config_string = StringIO()
    config.write(config_string)
    config_str = config_string.getvalue()
    print(config_str)
    with open(config_file, 'w') as f:
        config.write(f)
