#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LLS:
  """
  LSS   - Local Storage Server
  LSSC  - Local Storage Server Connection
  """
  ADDRESS = None
  CONNECTION = None

  @staticmethod
  def connect(address):
    raise NotImplementedError('LOCAL_STORAGE_SERVER_CONNECTION')


class Client:
  LOCAL_STORAGE_SERVER_CONNECTION = None

  @classmethod
  def set_LLS(cls, address):
    LLS.connect(address)
    cls.LOCAL_STORAGE_SERVER = LLS.CONNECTION

  def send_to_LSS(self, msg):
    if (self.LOCAL_STORAGE_SERVER_CONNECTION is None):
      raise ValueError('LLS not setted')

    self.LOCAL_STORAGE_SERVER_CONNECTION.send(msg)
