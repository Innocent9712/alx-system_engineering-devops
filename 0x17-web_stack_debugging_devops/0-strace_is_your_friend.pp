exec {'fix file extension':
  path    => ['/usr/bin', '/usr/local/bin', '/bin', '/usr/sbin'],
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
