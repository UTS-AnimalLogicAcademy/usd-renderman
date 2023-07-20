# -*- coding: utf-8 -*-

name = 'usd_renderman'

version = '2.1.1'

authors = ['ben.skinner', 'daniel.flood', 'jonah.newton']

build_requires = [
                  'python-2',
                  'cmake-3.2',
                  'boost_katana',
                  'tbb_katana',
		  'devtoolset-9'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'katana-4.5.2', 'rfk-24.4', 'renderman-24.4'],
    ['platform-linux', 'arch-x86_64', 'katana-4.5.2', 'rfk-25.0', 'renderman-25.0']
]

def commands():
    #env.KATANA_HOME.set('/opt/Foundry/Katana3.6v2')
    #env.KATANA_API_LOCATION.set(env.KATANA_HOME)
    #env.LD_LIBRARY_PATH.append('%s/bin' % env.KATANA_HOME)
    env.KATANA_RESOURCES.append('{root}/Resources')
