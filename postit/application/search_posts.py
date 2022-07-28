from typing import Optional, List, Tuple

import inject

from postit.domain.post import Post
from postit.domain.post_repository import PostRepository


class SearchPosts:
    @inject.autoparams()
    def __init__(self, database: PostRepository):
        self.__database = database

    def execute(self, start_after: Optional[int],
                end_before: Optional[int]) -> Tuple[List[Post], int]:
        results = self.__database.search_posts(start_after=start_after, end_before=end_before)
        count = self.__database.count_posts()

        return results, count
