# django_deploy
Django Project Deployement on GCP

```
pip install django-cors-headers

netstat -tlnp                                               # show open tcp ports

pip install gunicorn                                        # Install Gunicorn
gunicorn -b 0.0.0.0:8000 -w 3 deployment_project.wsgi       # -b = bind, -w = number of workers -d = daemon mode

sudo apt-get install nginx                                  # Install Nginx
vim /etc/nginx/sites-available/mysite                       # Configure Nginx to Pass Traffic with following

server {
    listen 8000;
    server_name 0.0.0.0;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
            root /home/prasad/env/django_deploy;
    }

    location / {
            include proxy_params;
            proxy_pass http://unix:/home/prasad/env/django_deploy/django_deploy.sock;
    }
}

# Add the nginx configurations to enabled sites of nginx
sudo ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled

sudo nginx -t         # Validate the configuration

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')     # Add this to djago_deploy/settings.py

python ./manage.py collectstatic                    # Collect Static files in project folder

sudo service nginx restart                          # Restart Nginx Server to take effect



# Let gunicorn communicate to nginx via unix socket
gunicorn --workers 3 --bind unix:/home/prasad/env/django_deploy/django_deploy.sock deployment_project.wsgi

Copy the Content of dist to /var/www/html/   # Server Static files
To change the static file path edit in /etc/nginx/sites-available/default

```
