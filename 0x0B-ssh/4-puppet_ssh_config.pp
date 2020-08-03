#SSH configuration file 
file_line { 'holberton':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}