#the verification the information
#is change the flie wp-config.php in option debug in true for identification error
#change the content in the file wp-settings for error identificatiion in debug
exec {'fix php ext.':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}
