#!/bin/bash
chmod 500 Feature_chip
chmod 500 Feature_gate1
chmod 500 Feature_gate2
sh cp.sh;
sh Process_Editor.sh;
sh CHIP_Edit.sh;
sh Gate_Analysizer.sh;
sh Gate_Level_Analysis.sh;
#python3 Gate_Level_Analysis.py