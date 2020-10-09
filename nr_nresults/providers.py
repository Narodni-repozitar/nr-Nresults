# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Thesis ID provider."""

from __future__ import absolute_import, print_function

from nr_common.providers import NRIdProvider


class NRNresultsIdProvider(NRIdProvider):
    """Thesss identifier provider."""

    pid_type = 'nrnrs'
    """Type of persistent identifier."""