# Overthewire Writeup

## Bandit Level

### Level 0
Simply using the command below, which connects to the server via ssh
`ssh bandit0@bandit.labs.overthewire.org -p 2220` when it asks for the password type `bandit0`. You may then proceed to Level 1.

### Level 1
The next task is to find the file "readme" stored in the home directory denoted by "~", you can easily get this by using "cat ~/readme".
Password = `boJ9jbbUNNfktd78OOpsqOltutMc3MY1`

### Level 2
The next level's password is stored in `~/-` which they make harder because you cannot directly do "cat -" as it reads the dash as an argument you can however escape this by using either `./-` or `~/-` like we've been doing.
Password = `CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9`

### Level 3
The next level's password is stored in the file `~/spaces in this filename` which we can escape if we put it in quotes.
`cat "spaces in this filename"`
Password = `UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK`

### Level 4
The password for the next level is stored in a hidden file in the inhere directory.
This can be found by using the command `ls -a` when you cd into it.
Password = `pIwrPrtPN36QITSp3EQaw936yaFoFgAB`

### Level 5
This password is found in the only human readable file which you can read each by doing something similar to `cat "./-file07"`, I did this manually going throgh each file until I got to file07.
Password = `koReBOKuIDDepwhWk7jZC0RTdopnAYKh`

### Level 6
The password file has the following properties.
human-readable
1033 bytes in size
not executable
This can be found with the find command using `find ./ -size 1033c` which finds a file of size 1033 bytes.
This finds "maybehere07/.file2".
Password = 
