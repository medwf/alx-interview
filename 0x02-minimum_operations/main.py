#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations



print(f"0 => {minOperations(-12)}")
print(f"0 => {minOperations(0)}")
print(f"0 => {minOperations(1)}")
print(f"6 => {minOperations(9)}")
print(f"6 => {minOperations(12)}")
print(f"10 => {minOperations(21)}")
print(f"19 => {minOperations(972)}")
print(f"326 => {minOperations(2147483640)}")
print(f"47613 => {minOperations(19170307)}")
