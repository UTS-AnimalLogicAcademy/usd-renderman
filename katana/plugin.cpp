// Copyright 2019 UTS Animal Logic Academy
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <usdKatana/attrMap.h>
#include <usdKatana/usdInPluginRegistry.h>

#include <pxr/usd/usdVol/volume.h>

#include "readUSDVolVolume.h"

PXR_NAMESPACE_USING_DIRECTIVE

// Might need to rename this op if usdKatana grows support for usdVol
USDKATANA_USDIN_PLUGIN_DECLARE(USDVolVolumeOp)
DEFINE_GEOLIBOP_PLUGIN(USDVolVolumeOp)
USDKATANA_USDIN_PLUGIN_DEFINE(
    USDVolVolumeOp, privateData, opArgs, interface) {
    readUSDVolVolume(interface, opArgs, privateData);
}

void registerPlugins() {
    USD_OP_REGISTER_PLUGIN(USDVolVolumeOp, "USDVolVolumeOp", 0, 1);
    UsdKatanaUsdInPluginRegistry::RegisterUsdType<UsdVolVolume>( "USDVolVolumeOp" );
}
