#!/usr/bin/env python3

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform


def main():
    """Run time code"""
    
    # create resp, which is our request object
    resp = requests.get(f"{API}sets")

    print( dir(resp) )


if __name__ == "__main__":
    main()
