# -*- coding: utf-8 -*-

name = 'usd_renderman'

version = '2.0.0'

authors = ['ben.skinner', 'daniel.flood', 'jonah.newton']

build_requires = [
                  'python',
                  'cmake-3.12+',
                  'KatanaUsdPlugins',
                  'boost_katana',
                  'tbb_katana'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'katana-4.5.2', 'rfk-24.4', 'renderman-24.4']
]

def commands():
    env.KATANA_RESOURCES.append('{root}/Resources')
