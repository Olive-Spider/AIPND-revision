#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Livya Kendi
# DATE CREATED: 3rd July 2023                                
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() - data structure that stores the command line arguments object  
    """
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--dir', type=str, default='pet_images', help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='text file with dog names')
    
    return parser.parse_args()

# Call the get_input_args() function to retrieve command line arguments
in_args = get_input_args()

# Access and print the values of the command line arguments
print("Argument 1:", in_args.dir)
print("Argument 2:", in_args.arch)
print("Argument 3:", in_args.dogfile)