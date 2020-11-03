import os
import sys

_BASE_PATH = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(_BASE_PATH)

def generate():
    git_url = 'https://github.com/ShemYu/learning-resource/blob/master'
    white_folder_list = ['reading']

    content_dict = {}

    for f_name in os.listdir():
        if f_name in white_folder_list:
            content_dict[f_name] = []
            md_name_list = [md_name.split('.')[0]
                            for md_name in os.listdir(f_name)]

            md_url_list = ['{}/{}/{}'.format(git_url, f_name, md_name)
                        for md_name in os.listdir(f_name)]
            for i, md_name in enumerate(md_name_list):
                content_line = '\t1. [{}]({})'.format(md_name, md_url_list[i])
                content_dict[f_name].append(content_line)

    content = '# Content\n\n'
    for section in content_dict:
        content += '- {}\n\n'.format(section)
        content += '\n\n'.join(content_dict[section])
        content += '\n\n'
    
    abstract = loading_readme_abstract()
    rdmd = open('README.md','w')
    rdmd.write(abstract+content)

def loading_readme_abstract():
    rdmd = open('README.md', 'r')
    rdmd.containt = rdmd.read()
    rdmd.abstract = rdmd.containt.split('# Content')[0]
    return rdmd.abstract

if __name__ == "__main__":
    generate()