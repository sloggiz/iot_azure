"""
===================================================================================================
Author:      Stepan Gaponiuk - D ONE 2023
Description: This script contains user input for streaming Raspberry Pi reed signal data into Azure
===================================================================================================
"""

# GPIO
LED_PIN = 4  # GPIO pin where the LED is connected to
SWITCH_PIN = 18  # GPIO pin where the reed switch is connected to

# Azure
IOT_HUB_CON_STR = "YOUR IOT HUB CONNECTION STRING"  # Paste your Azure IoT Hub connection string
DEVICE_IDPIC = "YOUR TOPIC NAME HERE"  # Paste your Azure IoT Hub device name
