# -*- coding: utf-8 -*-

name = 'usd_renderman'

version = '0.0.1'

authors = ['ben.skinner']

build_requires = [
                  'python',
                  'boost',
                  'usd',
                  'katana',
                  'usd_katana',
                  'tbb',
                  'rfk',
                  'renderman'
]

variants = [
    ['platform-linux', 'arch-x86_64', 'katana-3']
]

def commands():
    env.KATANA_RESOURCES.append('{root}/Resources')
