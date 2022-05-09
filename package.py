# -*- coding: utf-8 -*-

name = 'usd_renderman'

version = '1.0.2'

authors = ['ben.skinner', 'daniel.flood', 'jonah.newton']

build_requires = [
                  'python',
                  'cmake-3.12+',
                  'KatanaUsdPlugins',
                  'boost_katana',
                  'tbb_katana'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'katana-3.6.2', 'rfk-23.5', 'renderman-23.5'],
    ['platform-linux', 'arch-x86_64', 'katana-3.6.2', 'rfk-24', 'renderman-24'],
    ['platform-linux', 'arch-x86_64', 'katana-3.6.2', 'rfk-24', 'renderman-24.4']
]

def commands():
    env.KATANA_RESOURCES.append('{root}/Resources')
