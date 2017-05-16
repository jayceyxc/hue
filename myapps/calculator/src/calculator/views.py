#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import operator

from desktop.lib.django_util import render

OPS = dict(add=operator.add, subtract=operator.sub, multiply=operator.mul, divide=operator.truediv)
OP_STRING = dict(add="+", subtract="-", multiply="*", divide="/")


def index(request):
    if "op" not in request.REQUEST:
        return render('index.mako', request, dict())
    a = float(request.REQUEST["a"])
    b = float(request.REQUEST["b"])
    op = request.REQUEST["op"]
    result = OPS[op](a, b)
    return render("index.mako", request, dict(a=a, b=b, op=OP_STRING[op], result=result))
