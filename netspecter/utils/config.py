# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import configparser

def load() -> configparser.ConfigParser:
    c = configparser.ConfigParser()
    c.read("netspecter.cfg")
    return c
