# Correct Wordpress config misspelling
exec {'Correct Wordpress misspelling':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => shell,
}
