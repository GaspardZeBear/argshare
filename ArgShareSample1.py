import logging
from ArgShare import *

def foo(args) :
  logging.info('foo')
  logging.info(args.user)

def bar(args) :
  logging.info('bar')

#=====================================================================
logging.basicConfig(level=logging.DEBUG,\
      format='%(asctime)s %(module)s.%(funcName)s %(levelname)s -- %(message)s')

a=ArgShare(
  { 
    'subparsers' : [
       { 'id' : 'foo','func':foo , 'args' : ['user','password','fooOnly'] },
       { 'id' : 'bar','func':bar , 'args' : ['user','password','barOnly']}
    ],
    'arguments' : [
       { 'name' : 'fooOnly',  'apply' : lambda x: x.add_argument('-f','-fx','--fooOnly', action="store",help="fooOnly") },
       { 'name' : 'barOnly',  'apply' : lambda x: x.add_argument('-b','--barOnly', action="store",help="barOnly") },
       { 'name' : 'user',     'apply' : lambda x: x.add_argument('-u','--user', action="store",help="user") },
       { 'name' : 'password', 'apply' : lambda x: x.add_argument('-p','--password', action="store",help="password") },
    ]
  })

a.run()
