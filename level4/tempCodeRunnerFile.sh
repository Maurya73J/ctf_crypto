#!/usr/bin/expect
# set input_file "plaintext_pairs.txt"
# set filehandle [open $input_file r]
set log_file "output.log"

spawn ssh student@172.27.26.188
expect "password:"
send "cs641/r"
expect "Enter your group name:"
send "ciphereum"
expect "Enter password:"
send "mspciphereum"