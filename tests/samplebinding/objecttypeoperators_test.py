#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the Shiboken Python Bindings Generator project.
#
# Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
#
# Contact: PySide team <contact@pyside.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# version 2.1 as published by the Free Software Foundation. Please
# review the following information to ensure the GNU Lesser General
# Public License version 2.1 requirements will be met:
# http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
# #
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
from sample import *

class ObjectTypeOperatorsTest(unittest.TestCase):

    def testIt(self):
        a = ObjectTypeOperators("a")
        b = ObjectTypeOperators("b")
        self.assertFalse(a == b)
        self.assertEqual(a, a < b)

        # this should change a.key() and return nothing.
        self.assertEqual(None, a > b)
        self.assertEqual(a.key(), "aoperator>")

    def testPointerOpeators(self):
        a = ObjectTypeOperators("a")
        b = ObjectTypeOperators("b")
        self.assertEqual(a + "bc", "abc")
        self.assertEqual("bc" + a, "bca")
        self.assertEqual("a", a)
        self.assertEqual(a, "a")


if __name__ == '__main__':
    unittest.main()
