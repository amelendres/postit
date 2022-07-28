import inject

from postit.domain.post import Post
from postit.domain.post_repository import PostRepository


class GetPost:
    @inject.autoparams()
    def __init__(self, database: PostRepository):
        self.__database = database

    def execute(self, post_id: int) -> Post:
        return self.__database.get_post(post_id)
