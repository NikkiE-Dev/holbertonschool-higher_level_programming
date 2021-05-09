#!/usr/bin/python3
def best_score(a_dictionary):
   try:
      if len(a_dictionary) == 0:
         return None
      best =  max(a_dictionary, key=a_dictionary.get)
      return best

   except:
      return None
