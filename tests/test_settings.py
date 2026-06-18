from app import AppSettings


def test_settings_default_values() -> None:
    settings = AppSettings()
    assert settings.app_name == "python-base-template"
    assert settings.debug is False
