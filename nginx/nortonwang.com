server {
 listen 80;

 root /var/www/pelican;
 index index.html index.htm;

 location / {
  try_files $uri $uri/ /index.html;
  rewrite /about$ /about.html;
 }
}
