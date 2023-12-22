# install_flask.pp

class { 'python':
  version => '3.8.10',
}

package { 'python3-pip':
  ensure => present,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

exec { 'Fix URI.escape warning':
  command     => 'sed -i "s/URI.escape/URI::DEFAULT_PARSER.escape/" /path/to/your/puppet/modules',
  refreshonly => true,
  subscribe   => Package['python3-pip'],
}
