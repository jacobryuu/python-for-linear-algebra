from app import AppSettings


def test_settings_default_values() -> None:
    settings = AppSettings()
    assert settings.app_name == "python-for-linear-algebra"
    assert settings.debug is False
