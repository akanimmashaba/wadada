import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlmodel import SQLModel
from alembic import context
from settings.config import settings
from models.profile import Profile
from models.user_preference import UserPreference
from models.profile_models.children import Children
from models.profile_models.drinking import Drinking
from models.profile_models.education import Education
from models.profile_models.employment import Employment
from models.profile_models.gender import Gender
from models.profile_models.personality import Personality
from models.profile_models.pets import Pets
from models.profile_models.religion import Religion
from models.profile_models.seeking import Seeking
from models.profile_models.sexuality import Sexuality
from models.profile_models.smoking import Smoking
from models.profile_models.location import Location
from models.profile_models.image import Image
from models.profile_models.interests import Interest
from models.profile_models.language import Languages
from models.profile_models.relationship_status import RelationshipStatus

from models.subscription import PlanType, Discount, Transaction, Subscription
from models.match import Match
from models.message import Message
from models.notification import Notification
from models.report import Report
from models.swipe import Swipe 
from models.block import Block
from models.chatroom import ChatRoom

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = SQLModel.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
