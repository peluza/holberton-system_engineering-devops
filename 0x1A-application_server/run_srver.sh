#!/usr/bin/env bash
sudo service datadog-agent stop
cd ~/AirBnB_clone_v2
tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app'
tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'
cd ~/AirBnB_clone_v3
tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'
cd ~/AirBnB_clone_v4
tmux new-session -d 'gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app'
