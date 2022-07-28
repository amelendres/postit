import os

import inject
from flask import Flask

from postit.adapter.persistence.postgres_post_repository import PostgresPostRepository
from postit.domain.post_repository import PostRepository


def configure_application(application: Flask) -> None:
    application.config.update(
        DATABASE_URI=os.getenv('DATABASE_URI')
    )


def configure_inject(application: Flask) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(PostRepository, PostgresPostRepository(application.config['DATABASE_URI']))

    inject.configure(config)
