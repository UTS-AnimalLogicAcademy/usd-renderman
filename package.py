# -*- coding: utf-8 -*-

name = 'usd_renderman'

version = '3.1.0'

authors = ['ben.skinner', 'daniel.flood', 'jonah.newton']

build_requires = [
                  'cmake-3.16+',
                  'boost_katana',
                  'tbb_katana',
		  'devtoolset-9+'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'katana-6', 'rfk-26.0', 'renderman-26.0', 'python-3.9']
    
]

def commands():
    #env.KATANA_HOME.set('/opt/Foundry/Katana3.6v2')
    #env.KATANA_API_LOCATION.set(env.KATANA_HOME)
    #env.LD_LIBRARY_PATH.append('%s/bin' % env.KATANA_HOME)
    env.KATANA_RESOURCES.append('{root}/Resources')
