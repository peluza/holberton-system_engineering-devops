#!/usr/bin/env bash
#download letsencrypt (software the create certificate)
git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt
# stop service haproxy
service haproxy stop
#crete certificate ssl
/opt/letsencrypt/letsencrypt-auto certonly --standalone -d www.klase.tech -m 1597@holbertonschool.com --agree-tos
#creat folder for certificate
mkdir /etc/haproxy/certs
#transfer files at folder /etc/haproxy/certs
cat /etc/letsencrypt/live/www.klase.tech/fullchain.pem /etc/letsencrypt/live/www.klase.tech/privkey.pem >> /etc/haproxy/certs/www.klase.tech.pem
#create file txt for certificate ssl
echo "/etc/haproxy/certs/www.klase.tech.pem       www.klase.tech" >>  /etc/haproxy/certs/list.txt
#configure /etc/haproxy/haproxy.cfg
#frontend firstbalance
#	bind *:80
#	mode http
#	default_backend webservers
#
#frontend www-https
#   bind 0.0.0.0:443 ssl crt-list /etc/haproxy/certs/list.txt
#   reqadd X-Forwarded-Proto:\ https
#   acl letsencrypt-acl path_beg /.well-known/acme-challenge/
#   use_backend letsencrypt-backend if letsencrypt-acl
#   default_backend webservers
#
#backend webservers
#	balance roundrobin
#	mode http
#	option forwardfor
#	cookie SRVNAME insert nocache
#	server 1597-web-01 35.190.152.71:80 check
#	server 1597-web-01 34.75.218.253:80 check
#
#backend letsencrypt-backend
#   server letsencrypt 127.0.0.1:54321

#configure certificate for 2 moth
vi /opt/letsencrypt/renew.sh
# #!/bin/bash
#dominio=$1
#/opt/letsencrypt/letsencrypt-auto certonly --agree-tos --renew-by-default --standalone-supported-challenges http-01 --http-01-port 54321 -d $dominio
#cat /etc/letsencrypt/live/$dominio/fullchain.pem /etc/letsencrypt/live/$dominio/privkey.pem >> /etc/haproxy/certs/$dominio.pem
#service haproxy reload
chmod 755 /opt/letsencrypt/renew.sh
crontab -e
# add information
00 02 * */2 * /opt/letsencrypt/renew.sh
