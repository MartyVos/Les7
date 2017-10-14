cijfers = {"Benjamin": 9.7, "Marty": 9.1, "Bram": 9.1, "Denice": 8.2, "Brian": 8.4, "Eduard": 6.9, "Henk": 7.5, "Ivonne": 8.5}
for naam in cijfers:
    if cijfers.get(naam) > 9.0:
        print(naam, cijfers.get(naam))
