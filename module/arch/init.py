# encoding: utf-8

import conf
from fabric.api import *
from core.utils import utils
from module.common.init import init
class init(init):
	def install(self):
		super(init, self).prepare()
		with quiet():
			if (run('grep "/etc/profile.d" /etc/profile') == ""):
				put(conf.BASE_DIR + '/conf/init/profile.tpl', conf.BASE_DIR)
				run('cat ' + conf.BASE_DIR + '/profile.tpl >> /etc/profile')
		run('pacman -S base-devel --noconfirm --need')
		run('pacman -S wget --noconfirm --need')
		#run('apt-get install -y libncurses5-dev libxml2-dev zlib1g-dev libbz2-dev libmcrypt-dev libreadline-dev')
		#run('apt-get install -y libjpeg-dev libpng-dev libxpm-dev libfreetype6-dev libxslt1-dev libsasl2-dev')
		#run('apt-get install -y curl libcurl3 libcurl4-gnutls-dev libldap2-dev libpcre3 libpcre3-dev')
		super(init, self).install()