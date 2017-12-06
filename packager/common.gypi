# Copyright 2014 Google Inc. All rights reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd
#
# This file contains common settings for building packager components.

{
  'variables': {
    'variables': {
      'shaka_code%': 0,
    },
    'shaka_code%': '<(shaka_code)',
    'libpackager_type%': 'static_library',
    'conditions': [
      ['shaka_code==1', {
        # This enable warnings and warnings-as-errors.
        'chromium_code': 1,
      }],
    ],
  },
  'target_defaults': {
    'conditions': [
      ['shaka_code==1', {
        'include_dirs': [
          '.',
          '..',
        ],
        'conditions': [
          ['clang==1', {
            'cflags': [
              '-Wimplicit-fallthrough',
            ],
            # Revert the relevant settings in Chromium's common.gypi.
            'cflags!': [
              '-Wno-char-subscripts',
              '-Wno-unneeded-internal-declaration',
              '-Wno-covered-switch-default',

              # C++11-related flags:
              '-Wno-c++11-narrowing',
              '-Wno-reserved-user-defined-literal',
            ],
          }],
          ['OS == "win"', {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'WarnAsError': 'true',
                'DisableSpecificWarnings': ['4125']
              },
            },
          }],
        ],
      }, {
        'conditions': [
          # We do not have control over non-shaka code. Disable some warnings to
          # make build pass.
          ['clang==0', {
            'cflags': [
              '-Wno-dangling-else',
              '-Wno-deprecated-declarations',
              '-Wno-unused-function',
            ],
          }],
        ],
      }],
    ],
  },
}
