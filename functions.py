def unlimited_arguments(*args, **keyword_args):
    print(keyword_args)
    for key, value in keyword_args.items():
        print(key, value)


unlimited_arguments(1, 2, 3, 4, 5, 6, name='Oscar', age=22)
