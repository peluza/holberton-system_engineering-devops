# 0x1A. Application server

For this project, students are expected to look at these concepts:

- [Web Server](https://intranet.hbtn.io/concepts/17)
- [Server](https://intranet.hbtn.io/concepts/67)
- [Web stack debugging](https://intranet.hbtn.io/concepts/68)

## Background Context
[![ScreenShot](https://raw.github.com/GabLeRoux/WebMole/master/ressources/WebMole_Youtube_Video.png)](https://youtu.be/pSrKT7m4Ego)


Your web infrastructure is already serving web pages via Nginx that you installed in your [first web stack project](https://intranet.hbtn.io/rltoken/RrbqMLWOJUyVaWdXsnpvXw). While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

## Resources
### Read or watch:

- [Application server vs web server](https://intranet.hbtn.io/rltoken/RerpYBxsgrpIorHjbDgulw)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.hbtn.io/rltoken/uosy5QXdMbDPA1tFTR1eoA) (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
- [Running Gunicorn](https://intranet.hbtn.io/rltoken/QTnnkj6vfQV9ovW_eYWWDQ)
- [Be careful with the way Flask manages slash](https://intranet.hbtn.io/rltoken/whE8do28ZiJJoJLyb1ACwA) in [route](https://intranet.hbtn.io/rltoken/JLjrXD4MLS3rUkQr5QyxtA) - strict_slashes
- [Upstart documentation](https://intranet.hbtn.io/rltoken/oQPs-o5UUcZkxOw5sNIM0g)
## Requirements
### General

- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments

### Bash Scripts

- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing