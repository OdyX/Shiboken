/*
 * This file is part of the Shiboken Python Bindings Generator project.
 *
 * Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).
 *
 * Contact: PySide team <contact@pyside.org>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 */

#ifndef SBK_MODULE_H
#define SBK_MODULE_H

#include <Python.h>
#include "shibokenmacros.h"

namespace Shiboken {
namespace Module {

/**
 *  Imports and returns the module named \p moduleName, or a NULL pointer in case of failure.
 *  If the module is already imported, it increments its reference count before returning it.
 *  \returns the module specified in \p moduleName or NULL if an error occurs.
 */
LIBSHIBOKEN_API PyObject* import(const char* moduleName);

/**
 *  Creates a new Python module named \p moduleName using the information passed in \p moduleData.
 *  In fact, \p moduleData expects a "PyMethodDef*" object, but that's for Python 2. A void*
 *  was preferred to make this work with future Python 3 support.
 *  \returns a newly created module.
 */
LIBSHIBOKEN_API PyObject* create(const char* moduleName, void* moduleData);

/**
 *  Registers the list of types created by \p module.
 *  \param module   Module where the types were created.
 *  \param types    Array of PyTypeObject* objects representing the types created on \p module.
 */
LIBSHIBOKEN_API void registerTypes(PyObject* module, PyTypeObject** types);

/**
 *  Retrieves the array of types.
 *  \param module   Module where the types were created.
 *  \returns        A pointer to the PyTypeObject* array of types.
 */
LIBSHIBOKEN_API PyTypeObject** getTypes(PyObject* module);

} } // namespace Shiboken::Module

#endif // SBK_MODULE_H
