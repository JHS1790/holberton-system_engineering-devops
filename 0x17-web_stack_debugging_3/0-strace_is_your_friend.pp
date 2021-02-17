# Correct Wordpress config misspelling
exec {'Correct Wordpress misspelling':
  command  => 'sed -i "s+require_once( ABSPATH . WPINC . \'/class-wp-locale.phpp\' );\
              +require_once ( ABSPATH . WPINC . \'/class-wp-locale.php\' );+g" \
              /var/www/html/wp-settings.php',
  provider => shell,
}
