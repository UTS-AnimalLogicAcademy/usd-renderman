# -*- coding: utf-8 -*-

name = 'usd_renderman'

version = '0.0.5'

authors = ['ben.skinner', 'daniel.flood']

build_requires = [
                  'python',
                  'cmake-3.2',
                  'boost-1.55',
                  'usd_katana'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'katana-3.0.7', 'usd-19', 'tbb-4.4', 'rfk-22', 'renderman-22'],
    ['platform-linux', 'arch-x86_64', 'katana-3.0.7', 'usd-19', 'tbb-4.4', 'rfk-23', 'renderman-23']
]

def commands():
    env.KATANA_RESOURCES.append('{root}/Resources')
