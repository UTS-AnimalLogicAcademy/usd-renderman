# usd-renderman
Renderman specific integration for USD DCC Plugins used at the UTS Animal Logic Academy

## Goals
The primary goal of the repo at this point is to support the rendering of USDVol VDBAssets with Renderman in Katana. It is likely that we will find more purposes for this repo but for now support is limited to our needs in production.

## Building
We build everything with [rez](https://github.com/nerdvegas/rez).

### Requirements
Our current build requirements are
 * CMake-3.16+
 * Renderman-26.2
 * Katana-6.5.3
 * RendermanForKatana-26.2
 * USD-23.05 (included internally with Katana 6.5)
 * boost-1.76 (included internally with Katana 6.5)
 * tbb-2020.3 (included internally with Katana 6.5)
 * python-3.9

More work will be done to reduce and simplify build requirments if we have time.

## Contributing
We are still actively developing this repo as needed. However if there's any external interest in growing support for USD and Renderman, we'd be open accepting pull-requests. We'll add more documentation on how to do that, but for now, feel free to contact us directly or open an issue on GitHub!

## Acknowledgements
A lot of the usd - katana specific code is heavily influenced by Luma Picture's work with [usd-arnold](https://github.com/LumaPictures/usd-arnold).
