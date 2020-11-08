import os
import sys

_BASE_PATH = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(_BASE_PATH)

def generate():
    git_url = 'https://github.com/ShemYu/learning-resource/blob/master'
    white_folder_list = ['reading']

    content_dict = {}

    for f_name in os.listdir():
        if f_name in white_folder_list and os.listdir(f_name):
            # 資料夾名稱在白名單當中，且資料夾當中有檔案
            content_dict[f_name] = []
            # 取得所有檔案名稱，副檔名須為'md'
            md_name_list = [md_name.split('.')[0]
                            for md_name in os.listdir(f_name) if md_name.split('.')[-1] == 'md']
            # 產生超連結網址
            md_url_list = ['{}/{}/{}'.format(git_url, f_name, md_name.replace(' ', '%20'))
                        for md_name in os.listdir(f_name)]
            
            for i, md_name in enumerate(md_name_list):
                content_line = '\t1. [{}]({})'.format(md_name, md_url_list[i])
                content_dict[f_name].append(content_line)

    content = '# Contents\n\n'
    for section in content_dict:
        section_upper = section[0].upper()+section[1:]
        content += '- {}\n\n'.format(section_upper)
        content += '\n\n'.join(content_dict[section])
        content += '\n\n'
    
    abstract = loading_readme_abstract()
    rdmd = open('README.md','w')
    rdmd.write(abstract+content)

def loading_readme_abstract():
    rdmd = open('README.md', 'r')
    rdmd.containt = rdmd.read()
    rdmd.abstract = rdmd.containt.split('# Contents')[0]
    return rdmd.abstract

if __name__ == "__main__":
    generate()