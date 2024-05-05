from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TEST_SUITE_PATH: str
    JALIEN_SETUP_PATH: str
    SHARED_VOLUME: str

    model_config = SettingsConfigDict(env_file=".env")


SETTINGS = Settings()
