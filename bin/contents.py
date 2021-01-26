from autogencontens.transform import ReadingLoader


def generate(root_dir='reading'):
    rl = ReadingLoader()
    rl.get_structure()


if __name__ == "__main__":
    generate()