import random

candidates = ['가','나','다']

def pickOne(candidates: list):
    random.shuffle(candidates)
    picked=random.choice(candidates)
    candidates.remove(picked)
    print('후보', candidates, '\n',
          'picked', picked)

pickOne(candidates)

      
