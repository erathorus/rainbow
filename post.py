from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Post:
    title: str
    body: str
    date: datetime
    slug: str
    description: str
    categories: List[str]
    keywords: List[str]
    tags: List[str]

    def export_hugo(self):
        front_matter = dict()
        front_matter['title'] = Post.__as_toml_str(self.title)
        front_matter['date'] = Post.__as_toml_str(self.date.isoformat())
        front_matter['slug'] = Post.__as_toml_str(self.slug)
        front_matter['description'] = Post.__as_toml_str(self.description)
        front_matter['categories'] = Post.__as_toml_str_list(self.categories)
        front_matter['keywords'] = Post.__as_toml_str_list(self.keywords)
        front_matter['tags'] = Post.__as_toml_str_list(self.tags)

        s = '+++\n'
        for key, value in front_matter.items():
            s += f'{key} = {value}\n'
        s += '+++\n'
        s += '\n'
        s += self.body

        return s

    @staticmethod
    def __as_toml_str(s):
        return f'"{s}"'

    @staticmethod
    def __as_toml_str_list(entries):
        s = '['
        for i, entry in enumerate(entries):
            if i > 0:
                s += ', '
            s += Post.__as_toml_str(entry)
        s += ']'
        return s
