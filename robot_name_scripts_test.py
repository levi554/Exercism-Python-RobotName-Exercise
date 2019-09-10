import pytest
import robot_name_scripts


def main():

    def generate_random_number_test():
        random_name = robot_name_scripts.get_random_name()

        assert type(random_name) is str
        assert random_name is 'random1'

    generate_random_number_test()


if __name__ == '__main__':
    main()
