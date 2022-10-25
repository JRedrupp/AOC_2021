from __future__ import annotations

from fleet import Fleet


def main():
    """
    Main Entrypoint
    :return:
    """
    fleet = Fleet.from_file("input.txt")
    print(fleet.get_minimal_fuel_to_align())


if __name__ == '__main__':
    main()
