#Using puppet to just as in the previous configuration file task,
#we’d like you to set up your client SSH configuration file so that 
#you can connect to a server without typing a password.
exec { 'ssh_config':
	path => '/usr/bin',
	command => 'echo "IdentityFile ~/.ssh/school\ PasswordAuthentication no" >> /etc/ssh/ssh_config'
}
