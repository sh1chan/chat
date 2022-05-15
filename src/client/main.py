#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: bind RSS name to some id


class RSS:
  CONNECTIONS = {}

  @classmethod
  def load_from_rss(cls, name):
    raise NotImplementedError('Load saved RSS from given RSS')

  @classmethod
  def connect(cls, name, address):
    if name not in cls.CONNECTIONS:
      return None
    cls.CONNECTIONS[name] = 'socket.connect($address)'

  @classmethod
  def disconnect(cls):
    for connection in cls.CONNECTIONS.values():
      connection.close()


class Client:

  def send_to_LSS(self, msg):
    if (self.LOCAL_STORAGE_SERVER_CONNECTION is None):
      raise ValueError('LLS not setted')

    self.LOCAL_STORAGE_SERVER_CONNECTION.send(msg)


class ClientAPI:

  def add_RSS(self, name, address):
    RSS.connect(name, address)

  def get_RSS(self):
    return RSS.CONNECTIONS

  def set_RSS(cls, address):
    LLS.connect(lls_address)
    cls.LOCAL_STORAGE_SERVER_CONNECTION = LLS(address).connect()
