# -*- coding: utf-8 -*-

name = 'usd_renderman'

version = '2.0.3'

authors = ['ben.skinner', 'daniel.flood', 'jonah.newton']

build_requires = [
                  'python',
                  'cmake-3.2',
                  'KatanaUsdPlugins-19.11',
                  'boost_katana',
                  'tbb_katana'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'katana-4.5.2', 'rfk-24.4', 'renderman-24.4']
]

def commands():
    #env.KATANA_HOME.set('/opt/Foundry/Katana3.6v2')
    #env.KATANA_API_LOCATION.set(env.KATANA_HOME)
    #env.LD_LIBRARY_PATH.append('%s/bin' % env.KATANA_HOME)
    env.KATANA_RESOURCES.append('{root}/Resources')
