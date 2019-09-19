# -*- coding: utf-8 -*-

name = 'usd_renderman'

version = '0.0.4'

authors = ['ben.skinner']

build_requires = [
                  'python',
                  'boost',
                  'usd',
                  'usd_katana',
                  'tbb',
                  'rfk',
                  'renderman'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'katana-3.0.7'],
    ['platform-linux', 'arch-x86_64', 'katana-3.1.5']
]

def commands():
    env.KATANA_RESOURCES.append('{root}/Resources')
