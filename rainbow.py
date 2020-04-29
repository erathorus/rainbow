import pathlib
from typing import Dict

import contentful

from post import Post


class Rainbow:
    def __init__(self, store_id, access_token, content_directory):
        self.client = contentful.Client(store_id, access_token, timeout_s=60)
        self.content_directory = pathlib.Path(content_directory)

    def __fetch_posts(self) -> Dict[str, Post]:
        entries = self.client.entries()
        posts = dict()
        for entry in entries:
            post = Post(
                title=entry.title,
                body=entry.body,
                date=entry.updated_at,
                slug=entry.slug,
                description=getattr(entry, 'description', ''),
                categories=getattr(entry, 'categories', []),
                keywords=getattr(entry, 'keywords', []),
                tags=getattr(entry, 'tags', []),
            )
            posts[entry.id] = post
        return posts

    def save_posts(self):
        posts = self.__fetch_posts()
        self.content_directory.mkdir(parents=True, exist_ok=True)
        for post_id, post in posts.items():
            with open(self.content_directory.joinpath(f'{post_id}.md'), 'w') as f:
                f.write(post.export_hugo())
