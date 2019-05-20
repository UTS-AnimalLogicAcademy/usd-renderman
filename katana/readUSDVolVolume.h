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

#ifndef PXRUSDKATANA_READUSDVOLVOLUME_H
#define PXRUSDKATANA_READUSDVOLVOLUME_H

#include <pxr/pxr.h>

#include <usdKatana/usdInPrivateData.h>

PXR_NAMESPACE_OPEN_SCOPE

void readUSDVolVolume(
    FnKat::GeolibCookInterface& interface,
    FnKat::GroupAttribute opArgs,
    const PxrUsdKatanaUsdInPrivateData& privateData
);

PXR_NAMESPACE_CLOSE_SCOPE

#endif // PXRUSDKATANA_READUSDVOLVOLUME_H
