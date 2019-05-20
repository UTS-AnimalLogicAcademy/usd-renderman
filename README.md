# usd-renderman
Renderman specific integration for USD DCC Plugins used at the UTS Animal Logic Academy

## Goals
The primary goal of the repo at this point is to support the rendering of USDVol VDBAssets with Renderman in Katana. It is likely that we will find more purposes for this repo but for now support is limited to our needs in production.

## Building
We build everything with [rez](https://github.com/nerdvegas/rez).

### Requirements
Our current build requirements are
 * CMake-3.6.3
 * Renderman-22.5
 * Katana-3.1.1
 * RendermanForKatana-22.3
 * USD-19.01
 * boost-1.55
 * tbb-4.4.6
 * python-2.7.15

More work will be done to reduce and simplify build requirments if we have time.

## Acknowledgements
A lot of the usd - katana specific code is heavily influenced by Luma Picture's work with [usd-arnold](https://github.com/LumaPictures/usd-arnold).
