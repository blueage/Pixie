import wiringpi
import time
import os
import sys

chars = {
  " ": [
    "00000000",
    "00000000",
    "00000000",
    "00000000",
    "00000000"
  ],
  "!": [
    "00000000",
    "00000000",
    "01011111",
    "00000000",
    "00000000"
  ],
  "\"": [
    "00000000",
    "00000111",
    "00000000",
    "00000111",
    "00000000"
  ],
  "#": [
    "00010100",
    "01111111",
    "00010100",
    "01111111",
    "00010100"
  ],
  "$": [
    "00100100",
    "00101010",
    "01111111",
    "00101010",
    "00010010"
  ],
  "%": [
    "00100011",
    "00010011",
    "00001000",
    "01100100",
    "01100010"
  ],
  "&": [
    "00110110",
    "01001001",
    "01010101",
    "00100010",
    "01010000"
  ],
  "'": [
    "00000000",
    "00000101",
    "00000011",
    "00000000",
    "00000000"
  ],
  "(": [
    "00000000",
    "00011100",
    "00100010",
    "01000001",
    "00000000"
  ],
  ")": [
    "00000000",
    "01000001",
    "00100010",
    "00011100",
    "00000000"
  ],
  "*": [
    "00001000",
    "00101010",
    "00011100",
    "00101010",
    "00001000"
  ],
  "+": [
    "00001000",
    "00001000",
    "00111110",
    "00001000",
    "00001000"
  ],
  ",": [
    "00000000",
    "01010000",
    "00110000",
    "00000000",
    "00000000"
  ],
  "-": [
    "00001000",
    "00001000",
    "00001000",
    "00001000",
    "00001000"
  ],
  ".": [
    "00000000",
    "01100000",
    "01100000",
    "00000000",
    "00000000"
  ],
  "/": [
    "00100000",
    "00010000",
    "00001000",
    "00000100",
    "00000010"
  ],
  "0": [
    "00111110",
    "01010001",
    "01001001",
    "01000101",
    "00111110"
  ],
  "1": [
    "00000000",
    "01000010",
    "01111111",
    "01000000",
    "00000000"
  ],
  "2": [
    "01000010",
    "01100001",
    "01010001",
    "01001001",
    "01000110"
  ],
  "3": [
    "00100001",
    "01000001",
    "01000101",
    "01001011",
    "00110001"
  ],
  "4": [
    "00011000",
    "00010100",
    "00010010",
    "01111111",
    "00010000"
  ],
  "5": [
    "00100111",
    "01000101",
    "01000101",
    "01000101",
    "00111001"
  ],
  "6": [
    "00111100",
    "01001010",
    "01001001",
    "01001001",
    "00110000"
  ],
  "7": [
    "00000001",
    "01110001",
    "00001001",
    "00000101",
    "00000011"
  ],
  "8": [
    "00110110",
    "01001001",
    "01001001",
    "01001001",
    "00110110"
  ],
  "9": [
    "00000110",
    "01001001",
    "01001001",
    "00101001",
    "00011110"
  ],
  ":": [
    "00000000",
    "00110110",
    "00110110",
    "00000000",
    "00000000"
  ],
  ";": [
    "00000000",
    "01010110",
    "00110110",
    "00000000",
    "00000000"
  ],
  "<": [
    "00000000",
    "00001000",
    "00010100",
    "00100010",
    "01000001"
  ],
  "=": [
    "00010100",
    "00010100",
    "00010100",
    "00010100",
    "00010100"
  ],
  ">": [
    "01000001",
    "00100010",
    "00010100",
    "00001000",
    "00000000"
  ],
  "?": [
    "00000010",
    "00000001",
    "01010001",
    "00001001",
    "00000110"
  ],
  "@": [
    "00110010",
    "01001001",
    "01111001",
    "01000001",
    "00111110"
  ],
  "A": [
    "01111110",
    "00010001",
    "00010001",
    "00010001",
    "01111110"
  ],
  "B": [
    "01111111",
    "01001001",
    "01001001",
    "01001001",
    "00110110"
  ],
  "C": [
    "00111110",
    "01000001",
    "01000001",
    "01000001",
    "00100010"
  ],
  "D": [
    "01111111",
    "01000001",
    "01000001",
    "00100010",
    "00011100"
  ],
  "E": [
    "01111111",
    "01001001",
    "01001001",
    "01001001",
    "01000001"
  ],
  "F": [
    "01111111",
    "00001001",
    "00001001",
    "00000001",
    "00000001"
  ],
  "G": [
    "00111110",
    "01000001",
    "01000001",
    "01010001",
    "00110010"
  ],
  "H": [
    "01111111",
    "00001000",
    "00001000",
    "00001000",
    "01111111"
  ],
  "I": [
    "00000000",
    "01000001",
    "01111111",
    "01000001",
    "00000000"
  ],
  "J": [
    "00100000",
    "01000000",
    "01000001",
    "00111111",
    "00000001"
  ],
  "K": [
    "01111111",
    "00001000",
    "00010100",
    "00100010",
    "01000001"
  ],
  "L": [
    "01111111",
    "01000000",
    "01000000",
    "01000000",
    "01000000"
  ],
  "M": [
    "01111111",
    "00000010",
    "00000100",
    "00000010",
    "01111111"
  ],
  "N": [
    "01111111",
    "00000100",
    "00001000",
    "00010000",
    "01111111"
  ],
  "O": [
    "00111110",
    "01000001",
    "01000001",
    "01000001",
    "00111110"
  ],
  "P": [
    "01111111",
    "00001001",
    "00001001",
    "00001001",
    "00000110"
  ],
  "Q": [
    "00111110",
    "01000001",
    "01010001",
    "00100001",
    "01011110"
  ],
  "R": [
    "01111111",
    "00001001",
    "00011001",
    "00101001",
    "01000110"
  ],
  "S": [
    "01000110",
    "01001001",
    "01001001",
    "01001001",
    "00110001"
  ],
  "T": [
    "00000001",
    "00000001",
    "01111111",
    "00000001",
    "00000001"
  ],
  "U": [
    "00111111",
    "01000000",
    "01000000",
    "01000000",
    "00111111"
  ],
  "V": [
    "00011111",
    "00100000",
    "01000000",
    "00100000",
    "00011111"
  ],
  "W": [
    "01111111",
    "00100000",
    "00011000",
    "00100000",
    "01111111"
  ],
  "X": [
    "01100011",
    "00010100",
    "00001000",
    "00010100",
    "01100011"
  ],
  "Y": [
    "00000011",
    "00000100",
    "01111000",
    "00000100",
    "00000011"
  ],
  "Z": [
    "01100001",
    "01010001",
    "01001001",
    "01000101",
    "01000011"
  ],
  "[": [
    "00000000",
    "00000000",
    "01111111",
    "01000001",
    "01000001"
  ],
  "\\": [
    "00000010",
    "00000100",
    "00001000",
    "00010000",
    "00100000"
  ],
  "]": [
    "01000001",
    "01000001",
    "01111111",
    "00000000",
    "00000000"
  ],
  "^": [
    "00000100",
    "00000010",
    "00000001",
    "00000010",
    "00000100"
  ],
  "_": [
    "01000000",
    "01000000",
    "01000000",
    "01000000",
    "01000000"
  ],
  "`": [
    "00000000",
    "00000001",
    "00000010",
    "00000100",
    "00000000"
  ],
  "a": [
    "00100000",
    "01010100",
    "01010100",
    "01010100",
    "01111000"
  ],
  "b": [
    "01111111",
    "01001000",
    "01000100",
    "01000100",
    "00111000"
  ],
  "c": [
    "00111000",
    "01000100",
    "01000100",
    "01000100",
    "00100000"
  ],
  "d": [
    "00111000",
    "01000100",
    "01000100",
    "01001000",
    "01111111"
  ],
  "e": [
    "00111000",
    "01010100",
    "01010100",
    "01010100",
    "00011000"
  ],
  "f": [
    "00001000",
    "01111110",
    "00001001",
    "00000001",
    "00000010"
  ],
  "g": [
    "00001000",
    "00010100",
    "01010100",
    "01010100",
    "00111100"
  ],
  "h": [
    "01111111",
    "00001000",
    "00000100",
    "00000100",
    "01111000"
  ],
  "i": [
    "00000000",
    "01000100",
    "01111101",
    "01000000",
    "00000000"
  ],
  "j": [
    "00100000",
    "01000000",
    "01000100",
    "00111101",
    "00000000"
  ],
  "k": [
    "00000000",
    "01111111",
    "00010000",
    "00101000",
    "01000100"
  ],
  "l": [
    "00000000",
    "01000001",
    "01111111",
    "01000000",
    "00000000"
  ],
  "m": [
    "01111100",
    "00000100",
    "00011000",
    "00000100",
    "01111000"
  ],
  "n": [
    "01111100",
    "00001000",
    "00000100",
    "00000100",
    "01111000"
  ],
  "o": [
    "00111000",
    "01000100",
    "01000100",
    "01000100",
    "00111000"
  ],
  "p": [
    "01111100",
    "00010100",
    "00010100",
    "00010100",
    "00001000"
  ],
  "q": [
    "00001000",
    "00010100",
    "00010100",
    "00011000",
    "01111100"
  ],
  "r": [
    "01111100",
    "00001000",
    "00000100",
    "00000100",
    "00001000"
  ],
  "s": [
    "01001000",
    "01010100",
    "01010100",
    "01010100",
    "00100000"
  ],
  "t": [
    "00000100",
    "00111111",
    "01000100",
    "01000000",
    "00100000"
  ],
  "u": [
    "00111100",
    "01000000",
    "01000000",
    "00100000",
    "01111100"
  ],
  "v": [
    "00011100",
    "00100000",
    "01000000",
    "00100000",
    "00011100"
  ],
  "w": [
    "00111100",
    "01000000",
    "00110000",
    "01000000",
    "00111100"
  ],
  "x": [
    "01000100",
    "00101000",
    "00010000",
    "00101000",
    "01000100"
  ],
  "y": [
    "00001100",
    "01010000",
    "01010000",
    "01010000",
    "00111100"
  ],
  "z": [
    "01000100",
    "01100100",
    "01010100",
    "01001100",
    "01000100"
  ],
  "{": [
    "00000000",
    "00001000",
    "00110110",
    "01000001",
    "00000000"
  ],
  "|": [
    "00000000",
    "00000000",
    "01111111",
    "00000000",
    "00000000"
  ],
  "}": [
    "00000000",
    "01000001",
    "00110110",
    "00001000",
    "00000000"
  ],
  "~": [
    "00001000",
    "00001000",
    "00101010",
    "00011100",
    "00001000"
  ]
}

def send(data_pin, clk_pin, bits):
	wiringpi.wiringPiSetup()

	usleep = lambda x: time.sleep(x/1000000.0)

	wiringpi.pinMode(data_pin, 1)
	wiringpi.pinMode(clk_pin, 1)

	for item in bits:
        	wiringpi.digitalWrite(data_pin, int(item))
        	wiringpi.digitalWrite(clk_pin, 1)
        	usleep(12)
        	wiringpi.digitalWrite(clk_pin, 0)
        	usleep(12)

	time.sleep(0.01)

def write(dat_pin, clk_pin, num_pixies, input, system = "C"):
	out_bits = ""
	for item in input:
		out_bits += "00000000"
		out_bits += "11111111"
		out_bits += "00000000"
		out_bits += chars[item][0]
		out_bits += chars[item][1]
		out_bits += chars[item][2]
		out_bits += chars[item][3]
		out_bits += chars[item][4]

	while len(out_bits) < 128*num_pixies:
		out_bits = "0"+out_bits

	if system == "C":
		os.system("./pixie_write "+str(dat_pin)+" "+str(clk_pin)+" "+out_bits)
	else: # Python mode
		send(dat_pin, clk_pin, out_bits)
