# Setup nginx server
include nginx

nginx::resource::server { 'web1.emmastro.tech':
  listen_port => 80,
  proxy       => 'http://localhost:80',
}


file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
