from pizza import make_pizza as mp, build_profile;    
mp(16, 'pepperoni');
mp(12, 'mushrooms', 'green peppers', 'extra cheese');
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics');
print(user_profile);
print(mp.__name__);
print(mp.__doc__);