import logging
import argparse

#=====================================================================
#= argparse has a small problem with subparsers and arguments. 
#= Common arguments have to be set before the positionnal one.
#= I don'tt find this logical
#= This class permit to have only one definition of args 
#= applied to subparsers
#=====================================================================
class ArgShare() :

  #--------------------------------------------------------------------
  def __init__(self,parserDef) :
    self.parser = argparse.ArgumentParser()
    self.args={}
    for a in parserDef['arguments'] :
      self.args[a['name']]=a['apply']
    if 'subparsers' not in parserDef :
      for a in parserDef['arguments'] :
        a['apply'](self.parser)
    else :
      self.subparsers={}
      subparser = self.parser.add_subparsers()
      for s in parserDef['subparsers'] :
        self.subparsers[s['id']] = subparser.add_parser(s['id'])
        self.subparsers[s['id']].set_defaults(func=s['func'])
      for s in parserDef['subparsers'] :
        for a in s['args'] :
          self.args[a](self.subparsers[s['id']])
    self.args=self.parser.parse_args()

  #--------------------------------------------------------------------
  def getParser(self) :
    return(self.parser)

  #--------------------------------------------------------------------
  def getArgs(self) :
    return(self.args)

  #--------------------------------------------------------------------
  def run(self,f=None) :
    if f is None :
      self.args.func(self.args)
    else :
      f(self.args)
