import configparser
from io import StringIO
import GlobalVars
from GlobalVars import Settings
import inspect
import re

def findreplaceline(Find,value,lines):
    for i, line in enumerate(lines):
        # Check if the line starts with "OutSim Opts"
        if line.startswith(str(Find)):
            # Update the line
            lines[i] = str(str(Find)+" "+str(value))
            # Exit the loop
            break


from configparser import ConfigParser

class CaseSensitiveConfigParser(ConfigParser):
    def optionxform(self, optionstr):
        return optionstr



def readconfig():

    default_config = {}
    for class_name, class_obj in vars(Settings).items():
        if not class_name.startswith("__"):
            default_config[class_name] = {}
            # Iterate through the variables in each nested class
            for variable_name, variable_value in vars(class_obj).items():
                if not variable_name.startswith("__"):
                    default_config[class_name][variable_name] = variable_value

    print(default_config)

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
    #options = config.items('Settings')
    for section in config.sections():
        for option, value in config.items(section):
            if section in vars(Settings):
                try:
                    setattr(vars(Settings)[section], option, float(value))
                except ValueError:
                    setattr(vars(Settings)[section], option, value)

        #GlobalVars.Settings.__dict__[option]=value
        #GlobalVars.Settings.LFSSteerAngle = 77
       # print(GlobalVars.Settings.LFSSteerAngle)

def writeconfig():
    #global config
    config_file = 'FFBcountersteer.cfg'
    config = CaseSensitiveConfigParser()
    default_config = {}
    for class_name, class_obj in vars(Settings).items():
        if not class_name.startswith("__"):
            default_config[class_name] = {}
            # Iterate through the variables in each nested class
            for variable_name, variable_value in vars(class_obj).items():
                if not variable_name.startswith("__"):
                    default_config[class_name][variable_name] = variable_value
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

def patchLFScfg():



   try:
        with open(Settings.Main.LFS_cfg_location, "r") as file:
            # Read the contents of the file into memory and split by lines
            lines = file.read().split("\n")

        findreplaceline("OutSim Mode",2,lines)
        findreplaceline("OutSim Delay", 1, lines)
        findreplaceline("OutSim IP", "127.0.0.1", lines)
        findreplaceline("OutSim Port", 30000, lines)
        findreplaceline("OutSim ID", 0, lines)
        findreplaceline("OutSim Opts", 80, lines)
        # Rejoin the lines
        contents = "\n".join(lines)

        # Open the file for writing
        with open(Settings.Main.LFS_cfg_location, "w") as file:
            # Write the new contents to the file
            file.write(contents)
   except Exception:
        print("LFS cfg not patched!")

