#!/usr/bin/env python

from main import Client

def main():
  client = Client()
  client.set_LLS(444)

class A:
  __slots__ = ('hey',)
  hey = 3

if __name__ == '__main__':
  # main()
  a = A()
  print(a.hey)
  a.hey = 39
  print(a.hey)
