#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Shiboken Python Bindings Generator project.
#
# Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
#
# Contact: PySide team <contact@pyside.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# version 2.1 as published by the Free Software Foundation. Please
# review the following information to ensure the GNU Lesser General
# Public License version 2.1 requirements will be met:
# http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301 USA

import unittest

from sample import Overload, Str

class OverloadTest(unittest.TestCase):

    def testNoArgument(self):
        overload = Overload()
        self.assertEqual(overload.strBufferOverloads(), Overload.Function2)

    def testStrArgument(self):
        overload = Overload()
        self.assertEqual(overload.strBufferOverloads(Str('')), Overload.Function0)
        self.assertEqual(overload.strBufferOverloads(Str(''), ''), Overload.Function0)
        self.assertEqual(overload.strBufferOverloads(Str(''), '', False), Overload.Function0)

    def testStringArgumentAsStr(self):
        overload = Overload()
        self.assertEqual(overload.strBufferOverloads('', ''), Overload.Function0)
        self.assertEqual(overload.strBufferOverloads('', '', False), Overload.Function0)

    def testStringArgumentAsBuffer(self):
        overload = Overload()
        self.assertEqual(overload.strBufferOverloads('', 0), Overload.Function1)

    def testBufferArgument(self):
        overload = Overload()
        self.assertEqual(overload.strBufferOverloads(buffer(''), 0), Overload.Function1)

if __name__ == '__main__':
    unittest.main()

