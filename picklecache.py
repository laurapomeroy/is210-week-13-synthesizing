#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Picklecache"""


import os
import pickle


class PickleCache(object):
    """A constructor function that has two arguments.

    Args:
        file_path(str, opt): Defaults to datastore.pk1
        autosync(bool, optional): Defaults to False

    Attributes:
        __data: empty dictionary object.
    """
    def __init__(self, file_path='datastore.pk1', autosync=False):
        """Constructor

        Args:
            file_path(str, opt): constructor

        Attribute:
            autosync: a non-private attribute
        """
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """Saves the pair in the self.__data dictionary

        Args:
            key: required
            value: required
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """The length of self.__data

        Args:
            self: argument

        Returns:
            The length of self.__data
        """
        return len(self.__data)

    def __getitem__(self, key):
        """Takes one argument to return the requested value

        Args:
            key: required
        """
        try:
            return self.__data[key]
        except:
            raise KeyError('a key is not found')

    def __delitem__(self, key):
        """Removes any entries with the same key

        Args:
            key: required
        """
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Check if exists and is greater than 0
        """
        if os.path.exists(self.__file_path) is True and\
           os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """Save the data found"""
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
