# Slic3r-Project-To-STL

A Python script to extract STL files from an unsupported `.model` file format (similar to 3MF) from an early version of Slic3rPE.

## Background

My friend sent me some files to print, but they were in a strange zip containing no printable models. After digging around, I discovered it was an exported project from a very early version of Slic3rPE. The file format was an unsupported `.model` (something like 3MF, but not quite). 

## Solution

I wrote this Python script to extract the STL by copying the coordinates individually. It worked!

## Usage

1. Clone the repository.
2. Copy the .py file to the 3D folder containing `3dmodel.model` file
3. Run it.
4. Profit!

The script will generate an STL file from the unsupported `.model` format.

Feel free to use and modify this script for similar issues!
