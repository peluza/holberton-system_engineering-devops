#create a manifest that kills a process named killmenow.
exec {'killmenow':
  path    => '/usr/bin/env bash',
  command => 'pkill -f killmenow',
}
