facebook = {"ana", "luis", "marta", "pedro", "sofia", "julia"}
instagram = {"ana", "marta", "diego", "sofia", "lucia", "julia"}
twitter = {"ana", "tomas", "lucia", "carlos", "sofia", "pedro"}

en_las_tres = facebook & instagram & twitter

solo_facebook = facebook - instagram - twitter
solo_instagram = instagram - facebook - twitter
solo_twitter = twitter - facebook - instagram
solo_una = solo_facebook | solo_instagram | solo_twitter

al_menos_dos = (facebook & instagram) | (facebook & twitter) | (instagram & twitter)

print("Usan las tres plataformas:")
print(sorted(en_las_tres))

print("Usan solo una plataforma:")
print(sorted(solo_una))

print("Usan al menos dos plataformas:")
print(sorted(al_menos_dos))