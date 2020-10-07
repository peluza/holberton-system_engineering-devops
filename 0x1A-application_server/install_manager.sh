#!/usr/bin/env bash
apt-get update -y
apt-get upgrade -y
apt-get install python3-pip
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
pip3 install Flask
pip3 install flask_cors
apt-get install python3-dev
apt-get install libmysqlclient-dev
apt-get install zlib1g-dev
pip3 install mysqlclient==1.3.10
pip3 install SQLAlchemy==1.2.5
git clone https://github.com/peluza/AirBnB_clone_v3.git
cd ~/AirBnB_clone_v3 
cat setup_mysql_dev.sql | mysql -uroot -proot
cat setup_mysql_test.sql | mysql -uroot -proot
echo "install ok"
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=8421 python3 -m api.v1.app 
