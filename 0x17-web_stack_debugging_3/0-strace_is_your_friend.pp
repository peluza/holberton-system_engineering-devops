#change the content in the file wp-settings, the verification the information
#is change the flie wp-config.php in option debug in true for identification error
exec {'fix-wordpress':
  provider => shell,
  command  => 'sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php',
}
}
